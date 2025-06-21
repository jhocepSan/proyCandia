from domain.persona import service
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils import api_logger, api_telegram
import json
from domain.persona.schemas import PersonaCreate

router = APIRouter(
    prefix='/persona',
    tags=['persona']
)

@router.get("")
async def get():
    return service.get_all()

@router.post("")
async def crear_persona(nueva_persona: PersonaCreate):
    return service.crear_persona(nueva_persona)
