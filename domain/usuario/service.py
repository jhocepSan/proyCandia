from fastapi import HTTPException
import bcrypt
from utils.exceptions import DuplicatedError,DatabaseError
from . import repository
from .schemas import Usuario, UsuarioCreate

def validar_coneccion_db():
    try:
        result = repository.validar_coneccion()
        return True
    except Exception as error:
        return False

def crear_usuario(usuario: UsuarioCreate) -> Usuario:
    if validar_coneccion_db():
        found = repository.findByUsernameEmail(usuario.nombre, usuario.correo)
        if found:
            raise DuplicatedError(detail="El usuario ya existe")
        else:
            hashed_password = bcrypt.hashpw(usuario.contrasenia.encode('utf-8'), bcrypt.gensalt())
            usuario.contrasenia = hashed_password
            repository.add(usuario)
        found = repository.findByUsernameEmail(usuario.nombre, usuario.correo)
        usuario = Usuario(id=found['idusuario'], nombre=found['nameusuario'], correo=found['correo'],
                    tipo=found['tipo'],app=found['usoapp']).model_dump()
        return {"ok":usuario}
    else:
        raise DatabaseError(detail="Problemas con la base de datos")

def get_usuarios(skip: int = 0, limit: int = 100):
    if validar_coneccion_db():
        rows = repository.get_all(skip, limit)
        lista = [Usuario(
                id=data['idusuario'],
                nombre=data['nameusuario'],
                correo=data['correo'],
                tipo=data['tipo'],
                app=data['usoapp']).model_dump() for data in rows] if rows else []  
        return {'ok': lista}
    else:
        raise DatabaseError(detail="Problemas con la base de datos")
    


