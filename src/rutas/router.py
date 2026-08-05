import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, conint
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider

from src.skilling.router import handle_skilling_with_routes, UserInfo

from typing import List, Optional, Literal

from .prompt import RUTAS_PROMPT, RUTAS_USER_PROMPT, MISION_PROMPT, NEW_RUTAS_PROMPT, OBJECTIVE_SPECS

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

class RutasBody(BaseModel):
    questions: str #TODO: Cambiar a estructura de array de preguntas si es necesario

#Esto es por mientras para probar la estructura de preguntas
class QuestionsStructure(BaseModel):
    genero: str
    edad: str
    situacion_laboral: str
    industria: str
    tipo_rol: str
    objetivo_profesional: str
    has_pensado_proposito: str
    proposito_vida: str


class Dia(BaseModel):
    numero: conint(ge=1, le=5)
    tiempo_estimado_min: conint(ge=15, le=50)
    instrucciones: List[str] = Field(min_length=2, max_length=6)
    entregable: str

class Semana(BaseModel):
    numero: conint(ge=1, le=8)
    titulo: str  # ej. "Entender tu situación actual como líder"
    resultado_semana: str
    habilidades_conocimientos: List[str] = Field(min_length=1, max_length=3)
    dias: List[Dia] = Field(min_length=5, max_length=5)

class Mes(BaseModel):
    numero: conint(ge=1, le=2)
    titulo: str  # ej. "Claridad profunda sobre el cambio"
    resultado_mes: str
    semanas: List[Semana]

class NewRutasResponse(BaseModel):
    titulo: str  # "Plan de trabajo · [Objetivo seleccionado]"
    subtitulo: str  # "Adaptado al perfil de ... "
    objetivo_seleccionado: str
    meses: List[Mes] = Field(min_length=2, max_length=2)

estructure_agent = Agent(model, system_prompt="Eres un asistente que ayuda a estructurar las siguientes preguntas en un formato JSON con las siguientes llaves: genero, edad, situacion_laboral, industria, tipo_rol, objetivo_profesional, has_pensado_proposito, proposito_vida. Responde solo con el JSON solicitado.", result_type=QuestionsStructure)

new_rutas_agent = Agent(
    model, 
    system_prompt=NEW_RUTAS_PROMPT, 
    result_type=NewRutasResponse,
    retries=3
)

@router.post('/rutas-old')
async def handle_rutas_old_message(body: Body):
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
    
@router.post('/rutas')
async def handle_rutas_message(body: RutasBody):
    try:
        print("Corriendo")
        real_estructure = await estructure_agent.run(body.questions)

        user_info = real_estructure.data

        objective_specifications = OBJECTIVE_SPECS.get(user_info.objetivo_profesional.lower(), None)

        objective_specifications_str = ""
        if objective_specifications:
            objective_specifications_str = f"""
            Especificaciones del objetivo profesional:
            Perfil de entrada (antes del plan): {objective_specifications.get('entry_profile', '')}

            Perfil de salida (después del plan): {objective_specifications.get('exit_profile', '')}

            Competencias desarrolladas al finalizar el plan: {objective_specifications.get('skills_knowledge_outcomes', '')}
            """

        # objective_example = OBJECTIVE_EXAMPLES.get(user_info.objetivo_profesional.lower(), "")
        
        user_prompt = f"""
        Preguntas y respuestas del usuario:
        - Género: {user_info.genero}
        - Edad: {user_info.edad}
        - Situación laboral: {user_info.situacion_laboral}
        - Industria: {user_info.industria}
        - Tipo de rol: {user_info.tipo_rol}
        - Objetivo profesional: {user_info.objetivo_profesional}
        - ¿Has pensado en tu propósito de vida?: {user_info.has_pensado_proposito}
        - Propósito de vida: {user_info.proposito_vida}

        {objective_specifications_str}
        """

        # user_prompt_con_ejemplo = f"""
        # Preguntas y respuestas del usuario:
        # - Género: {user_info.genero}
        # - Edad: {user_info.edad}
        # - Situación laboral: {user_info.situacion_laboral}
        # - Industria: {user_info.industria}
        # - Tipo de rol: {user_info.tipo_rol}
        # - Objetivo profesional: {user_info.objetivo_profesional}
        # - ¿Has pensado en tu propósito de vida?: {user_info.has_pensado_proposito}
        # - Propósito de vida: {user_info.proposito_vida}

        # Especificaciones del objetivo profesional:
        # Perfil de entrada (antes del plan): {objective_specifications.get('entry_profile', '')}

        # Perfil de salida (después del plan): {objective_specifications.get('exit_profile', '')}

        # Competencias desarrolladas al finalizar el plan: {objective_specifications.get('skills_knowledge_outcomes', '')}

        # Este es un ejemplo de plan en el cual te puedes basar:
        # {objective_example}
        # """

        complete_plan = await new_rutas_agent.run(user_prompt)

        # complete_plan_con_ejemplo = await new_rutas_agent.run(user_prompt_con_ejemplo)

        return complete_plan.data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/mision')
async def handle_mision_message(body: MisionBody):
    try:
        response = await mision_agent.run(str(body))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))