from fastapi import HTTPException
import bcrypt
from utils.exceptions import DuplicatedError
from . import repository
from .schemas import Usuario, UsuarioCreate


def crear_usuario(usuario: UsuarioCreate) -> Usuario:
    found = repository.findByUsernameEmail(usuario.nombre, usuario.correo)
    if found:
        raise DuplicatedError(detail="El usuario ya existe")
    else:
        hashed_password = bcrypt.hashpw(usuario.contrasenia.encode('utf-8'), bcrypt.gensalt())
        usuario.contrasenia = hashed_password
        repository.add(usuario)
    found = repository.findByUsernameEmail(usuario.nombre, usuario.correo)
    return Usuario(id=found['idusuario'], nombre=found['nameusuario'], correo=found['correo'],
                   tipo=found['tipo'],app=found['usoapp']).model_dump()


def get_usuarios(skip: int = 0, limit: int = 100):
    rows = repository.get_all(skip, limit)
    return [Usuario(
            id=data['idusuario'],
            nombre=data['nameusuario'],
            correo=data['correo'],
            tipo=data['tipo'],
            app=data['usoapp']).model_dump() for data in rows] if rows else []
    


