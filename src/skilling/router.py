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

from .prompt import SKILLING_PROMPT

load_dotenv()

router = APIRouter()

class UsedTool(BaseModel):
    tool: str
    toolInput: str
    toolOutput: str

class AdditionalRecomendation(BaseModel):
    platform: str
    search_url: str

class PrimaryRecomendation(BaseModel):
    product_name: str
    program_type: str
    format: str
    link: str
    description: str
    offer: str
    reason: str

class ParsedText(BaseModel):
    primary_recomendations: List[PrimaryRecomendation]
    additional_recomendations: List[AdditionalRecomendation]
    categories: List[str]
    
class ParsedObject(BaseModel):
    text: ParsedText
    usedTools: List[UsedTool]
    question: str
    chatId: str
    chatMessageId: str
    isStreamValid: bool
    sessionId: str
    memoryType: str


API_URL = "https://flowise2.tecmilab.com.mx/api/v1/prediction/66f7a428-49a0-4a33-9428-70c1ed5b429b"

provider = AzureProvider(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version='2024-12-01-preview',
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = OpenAIModel('gpt-4o', provider=provider)
skilling_agent = Agent(model, system_prompt=SKILLING_PROMPT, result_type=ParsedText)

class Body(BaseModel):
    question: str

@router.post('/skilling')
async def handle_skilling_query(body: Body):
    try:
        # Primero obtenemos la respuesta de Flowise
        flowise_response = requests.post(API_URL, json={"question": body.question})
        flowise_data = flowise_response.json()

        print("flowise_data", flowise_data)

        print ("flowise_data['text']", flowise_data['text'])
        
        # Usamos el agente solo para parsear el campo text
        parsed_text = await skilling_agent.run(flowise_data['text'])

        print("parsed_text", parsed_text)

        return {
            "text": parsed_text.data.dict(),
            "usedTools": flowise_data['usedTools'],
            "question": flowise_data['question'],
            "chatId": flowise_data['chatId'],
            "chatMessageId": flowise_data['chatMessageId'],
            "isStreamValid": flowise_data['isStreamValid'],
            "sessionId": flowise_data['sessionId'],
            "memoryType": flowise_data['memoryType']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
