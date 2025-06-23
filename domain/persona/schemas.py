from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PersonaBase(BaseModel):
    idpersona: int


class PersonaCreate(BaseModel):
    nombres: str
    apellidos: str
    direccion: Optional[str]
    telefono: Optional[str]
    codigo: Optional[str]


class Persona(PersonaBase):
    idusuario: int
    nombres: str
    apellidos: str
    direccion: Optional[str]
    telefono: Optional[int]
    codigo: Optional[str]
    foto: Optional[str]
    estado: Optional[str]
    tipo: Optional[str]
    fecha: datetime
