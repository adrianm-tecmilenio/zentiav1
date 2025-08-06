import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider

from src.skilling.router import handle_skilling_with_routes, UserInfo

from typing import Literal

from .prompt import RUTAS_PROMPT, RUTAS_USER_PROMPT, MISION_PROMPT

load_dotenv()

router = APIRouter()

class Mision(BaseModel):
    nombre: str
    descripcion: str
    tipo: Literal["textField", "imagen"]
    tiempo: str
    complejidad: Literal["low", "medium", "high"]


class Fase(BaseModel):
    nombre: str
    objetivo: str
    misiones: list[Mision]
    reflexion: str
    checkpoint: str

class AgentResponse(BaseModel):
    nombre_reto: str
    objetivo: str
    fase1: Fase
    fase2: Fase
    fase3: Fase

class MisionResponse(BaseModel):
    mision: Mision
      

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o-zentia', provider=provider)
rutas_agent = Agent(model, system_prompt=RUTAS_PROMPT, result_type=AgentResponse)
mision_agent = Agent(model, system_prompt=MISION_PROMPT, result_type=MisionResponse)

#TOOD: cambiar la estructura de cómo se recibe información (cambio en areas, estructura de preguntas)
class Body(BaseModel):
    arquetipo: Literal["planeador", "fantasioso", "generalista", "autonomo"]
    meta: str
    proposito: str
    preguntas: list[str]

class MisionBody(BaseModel):
    arquetipo: Literal["planeador", "fantasioso", "generalista", "autonomo"]
    meta: str
    proposito: str

@router.post('/rutas')
async def handle_rutas_message(body: Body):
    try:
        user_info = UserInfo(
            meta=body.meta,
            proposito=body.proposito,
            preguntas=body.preguntas
        )

        courses = await handle_skilling_with_routes(user_info)
        
        response = await rutas_agent.run(RUTAS_USER_PROMPT.format(user_info=user_info, cursos=courses))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/mision')
async def handle_mision_message(body: MisionBody):
    try:
        response = await mision_agent.run(str(body))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))