import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider

from .prompt import GENERADOR_PROMPT

load_dotenv()

router = APIRouter()

class Proposito(BaseModel):
    purpose: str

class AgentResponse(BaseModel):
    misuse: bool
    purposes: list[Proposito]

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o', provider=provider)
generador_agent = Agent(model, system_prompt=GENERADOR_PROMPT, result_type=AgentResponse)

class Body(BaseModel):
    message: str

@router.post('/generador')
async def handle_generador_message(body: Body):
    try:
        response = await generador_agent.run(body.message)
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 