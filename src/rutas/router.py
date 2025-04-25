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

class Mision(BaseModel):
    tipo: Literal["habito", "enfoque", "skill"]
    titulo: str
    instrucciones: str

#TODO: Cambiar a mision por tipo

class RutaProposito(BaseModel):
    ruta: str
    misiones: list[Mision]

class RutaExploradora(BaseModel):
    ruta: str
    misiones: list[Mision]

class RutaIntrepida(BaseModel):
    ruta: str
    misiones: list[Mision]

class AgentResponse(BaseModel):
    ruta_proposito: RutaProposito
    ruta_exploradora: RutaExploradora
    ruta_intrepida: RutaIntrepida

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o-zentia', provider=provider)
rutas_agent = Agent(model, system_prompt=RUTAS_PROMPT, result_type=AgentResponse)

class Body(BaseModel):
    # message: str
    areas: list[str]
    proposito: str

@router.post('/rutas')
async def handle_rutas_message(body: Body):
    try:
        response = await rutas_agent.run(str(body))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
