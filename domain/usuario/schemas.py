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

class UpdateUser(BaseModel):
    id:int
    nombre: Optional[str]
    correo:str
    tipo:Optional[str]
    app:Optional[str]

class Usuario(UsuarioBase):
    nombre: Optional[str]
    correo: str
    tipo: Optional[str]
    app: Optional[str]
    estado:Optional[str]
    nametipo:Optional[str]
    nameapp:Optional[str]
    nameestado:Optional[str]

class ChangeEstadoUser(UsuarioBase):
    estado :str