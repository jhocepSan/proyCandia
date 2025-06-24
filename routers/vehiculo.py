from domain.vehiculo import service
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils import api_logger, api_telegram
from domain.vehiculo.schemas import VehiculoCreate, Vehiculo

router = APIRouter(
    prefix='/vehiculo',
    tags=['vehiculo']
)

@router.get("")
async def get() -> list[Vehiculo]:
    return service.get_all()

@router.post("")
async def post(data: VehiculoCreate) -> Vehiculo:
    return service.crear_vehiculo(data)
