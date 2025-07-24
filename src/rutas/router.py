import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider

from typing import Literal

from .prompt import RUTAS_PROMPT

load_dotenv()

router = APIRouter()

class Fase(BaseModel):
    misiones: list[str]
    reflexion: str
    pregunta_clave: str

class AgentResponse(BaseModel):
    nombre_reto: str
    objetivo: str
    fase1: Fase
    fase2: Fase
    fase3: Fase
      

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o-zentia', provider=provider)
rutas_agent = Agent(model, system_prompt=RUTAS_PROMPT, result_type=AgentResponse)

class Body(BaseModel):
    arquetipo: Literal["explorador", "alma", "corazon"]
    area: Literal["proposito", "profesional", "intelectual", "finanzas"]
    meta: str
    proposito: str

@router.post('/rutas')
async def handle_rutas_message(body: Body):
    try:
        response = await rutas_agent.run(str(body))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
