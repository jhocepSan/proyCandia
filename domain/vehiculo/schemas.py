from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoVehiculo(BaseModel):
    id: int
    nombre: str
    estado: str

class VehiculoBase(BaseModel):
    id: int


class VehiculoCreate(BaseModel):
    modelo: Optional[str]
    placa: str
    color: Optional[str]
    tipoId: Optional[int]
    tipoNombre: Optional[str]
    motor: Optional[str]
    km: Optional[str]
    fotoplaca: Optional[str]
    foto: Optional[str]


class Vehiculo(VehiculoBase):
    modelo: Optional[str]
    placa: str
    color: Optional[str]
    tipo: Optional[TipoVehiculo]
    motor: Optional[str]
    km: Optional[str]
    fotoplaca: Optional[str]
    foto: Optional[str]
    fecha: datetime
