import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider
from src.vector_db import query_vectors
from langchain_openai import AzureOpenAIEmbeddings

from .prompt import OMI_PROMPT

load_dotenv()

router = APIRouter()

class AgentResponse(BaseModel):
    message: str

provider = AzureProvider(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version='2024-12-01-preview',
        api_key=os.getenv("OPENAI_API_KEY"),
    )

model = OpenAIModel('gpt-4o-zentia', provider=provider)
omi_agent = Agent(model, system_prompt=OMI_PROMPT, result_type=AgentResponse)

# Inicializar embeddings
embeddings = AzureOpenAIEmbeddings(
    dimensions=1024,
    model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_version=os.getenv("OPENAI_API_VERSION")
)

class Body(BaseModel):
    message: str
    proposito: str

async def get_relevant_context(query: str, top_k: int = 3) -> str:
    """
    Obtiene contexto relevante de Pinecone para la consulta.
    """
    query_embedding = embeddings.embed_query(query)
    results = query_vectors("zentia-faq", query_embedding, top_k=top_k)
    
    if not results.matches:
        return ""
        
    # Construir contexto
    context = "\n".join([match.metadata["text"] for match in results.matches])
    return context

@router.post('/omi')
async def handle_omi_message(body: Body):
    try:
        # Obtener contexto relevante de Pinecone
        context = await get_relevant_context(body.message)
        
        if context:
            # Si hay contexto relevante, crear un prompt que combine la personalidad con la información
            prompt = f"""Contexto relevante:
            {context}

            Mensaje del usuario: {body.message}

            Por favor, responde manteniendo tu personalidad de Omi (monje sabio y empático) pero utilizando la información del contexto cuando sea relevante. 
            Si el contexto no es completamente relevante, responde principalmente con tu personalidad y usa el contexto solo si ayuda a la conversación.
            """
        else:
            # Si no hay contexto relevante, usar el mensaje original
            prompt = body.message

        response = await omi_agent.run(prompt)
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))