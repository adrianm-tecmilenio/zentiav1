import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from src.agent import agent_router
from src.omi import omi_router
from src.rutas import rutas_router
from src.generador import generador_router
from src.skilling import router_skilling
from src.endpoints import router as vector_router

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Bienvenido a zentia'}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(omi_router, tags=['omi'])
app.include_router(rutas_router, tags=['rutas'])
app.include_router(generador_router, tags=['generador'])
app.include_router(router_skilling, tags=['skilling'])
app.include_router(vector_router, tags=['vector'])