from domain.usuario import service
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils import api_logger, api_telegram
import json
from domain.usuario.schemas import UsuarioCreate

router = APIRouter(
    prefix='/usuario',
    tags=['usuario']
)

@router.get("")
async def get_usuarios():
    return service.get_usuarios()

@router.post("")
async def crear_usuario(nuevo_usuario: UsuarioCreate):
    return service.crear_usuario(nuevo_usuario)