import os
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.azure import AzureProvider
from typing import List
from src.scripts import get_palabras_clave_unicas
from typing import Literal

from .prompt import SKILLING_PROMPT, SELECTOR_PROMPT, SELECTOR_USER_PROMPT
from .course_search import CourseSearch

load_dotenv()

router = APIRouter()

class Response(BaseModel):
    palabras_clave: list[str]

class CourseRecommendation(BaseModel):
    titulo: str
    enlace: str
    precio_actual: str
    precio_original: str
    palabras_clave: str
    score_relevancia: float
    palabras_coincidentes: List[str]

class SelectorResponse(BaseModel):
    cursos_recomendados: list[CourseRecommendation]

class SkillingWithCoursesResponse(BaseModel):
    palabras_clave: List[str]
    cursos_recomendados: List[CourseRecommendation]

palabras_clave = get_palabras_clave_unicas()

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o-zentia', provider=provider)
skilling_agent = Agent(model, system_prompt=SKILLING_PROMPT.format(palabras_clave=palabras_clave), result_type=Response)
selector_agent = Agent(model, system_prompt=SELECTOR_PROMPT, result_type=SelectorResponse)

# Inicializar el buscador de cursos
course_searcher = CourseSearch()

class UserInfo(BaseModel):
    meta: str
    proposito: str
    preguntas: list[str]

class Body(BaseModel):
    user_info: UserInfo

@router.post('/skilling')
async def handle_skilling_query(body: UserInfo):
    try:
        # Usamos el agente solo para parsear el campo text
        response = await skilling_agent.run(str(body))
        
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/skilling-with-routes')
async def handle_skilling_with_routes(body: UserInfo):
    """
    Endpoint que combina la respuesta del agente de skilling con recomendaciones de cursos
    """
    try:
        # Obtener palabras clave del agente
        response = await skilling_agent.run(str(body))
        palabras_clave = response.data.palabras_clave
        
        # Buscar cursos basándose en las palabras clave
        cursos_encontrados = course_searcher.search_courses_by_keywords(palabras_clave, max_results=10)
        
        # Convertir los cursos encontrados al formato de respuesta
        cursos_recomendados = []
        for curso in cursos_encontrados:
            cursos_recomendados.append(CourseRecommendation(
                titulo=curso['titulo'],
                enlace=curso['enlace'],
                precio_actual=curso['precio_actual'],
                precio_original=curso['precio_original'],
                palabras_clave=curso['palabras_clave'],
                score_relevancia=curso['score_relevancia'],
                palabras_coincidentes=curso['palabras_coincidentes']
            ))



        response = await selector_agent.run(SELECTOR_USER_PROMPT.format(user_info=str(body), cursos=str(cursos_recomendados)))

        return SkillingWithCoursesResponse(
            palabras_clave= palabras_clave,
            cursos_recomendados=response.data.cursos_recomendados
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/courses/search')
async def search_courses_by_keywords(keywords: str, max_results: int = 10):
    """
    Endpoint para buscar cursos directamente por palabras clave
    """
    try:
        # Separar las palabras clave por comas
        keyword_list = [kw.strip() for kw in keywords.split(',') if kw.strip()]
        
        if not keyword_list:
            raise HTTPException(status_code=400, detail="Debe proporcionar al menos una palabra clave")
        
        cursos_encontrados = course_searcher.search_courses_by_keywords(keyword_list, max_results)
        
        return {
            "palabras_clave_busqueda": keyword_list,
            "cursos_encontrados": cursos_encontrados,
            "total_resultados": len(cursos_encontrados)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/courses/all')
async def get_all_courses():
    """
    Endpoint para obtener todos los cursos disponibles
    """
    try:
        cursos = course_searcher.get_all_courses()
        return {
            "total_cursos": len(cursos),
            "cursos": cursos
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/courses/category/{category}')
async def get_courses_by_category(category: str):
    """
    Endpoint para obtener cursos por categoría
    """
    try:
        cursos = course_searcher.get_courses_by_category(category)
        return {
            "categoria": category,
            "total_cursos": len(cursos),
            "cursos": cursos
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
