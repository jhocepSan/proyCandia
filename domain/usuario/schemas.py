from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    id: int


class UsuarioCreate(BaseModel):
    nombre: Optional[str]
    correo: str
    tipo: Optional[str]
    app: Optional[str]
    contrasenia: str


class Usuario(UsuarioBase):
    nombre: str
    correo: str
    tipo: Optional[str]
    app: Optional[str]