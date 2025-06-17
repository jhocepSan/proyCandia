from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from domain.usuario.schemas import Usuario

class SignIn(BaseModel):
    usuario: str
    contrasena: str


class SignInResponse(BaseModel):
    access_token: str
    expiration: datetime
    user_info: Usuario
