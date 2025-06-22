from domain.usuario import service
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils import api_logger, api_telegram
import json
from domain.usuario.schemas import UsuarioCreate,UpdateUser,ChangeEstadoUser

router = APIRouter(
    prefix='/usuario',
    tags=['usuario']
)

@router.get("")
async def get_usuarios():
    result =  service.get_usuarios()
    return JSONResponse(status_code=200, content=result)

@router.post("")
async def crear_usuario(nuevo_usuario: UsuarioCreate):
    result = service.crear_usuario(nuevo_usuario) 
    return JSONResponse(status_code=200, content=result)
@router.post("/update")
async def update_usuario(usuario:UpdateUser):
    result = service.update_user(usuario)
    return JSONResponse(status_code=200,content=result)

@router.post("/changeEstado")
async def change_estado(usuario:ChangeEstadoUser):
    result = service.change_estado_user(usuario)
    return JSONResponse(status_code=200,content=result)