from fastapi import HTTPException, status
import bcrypt
from utils.exceptions import DuplicatedError
from . import repository
from .schemas import Persona, PersonaCreate

def validar_coneccion_db():
    try:
        result = repository.validar_coneccion()
        return True
    except Exception as error:
        return False

def crear_persona(data: PersonaCreate) -> Persona:
    if validar_coneccion_db():
        #found = repository.find_by_codigo(data.codigo)
        found = None
        if found:
            raise DuplicatedError(detail="La persona ya existe")
        persona = repository.add(data)
        persona = Persona(idpersona=persona['idpersona'], 
                          idusuario=persona['idusuario'], 
                          nombres=persona['nombres'], 
                          apellidos=persona['apellidos'],
                          direccion=persona['direccion'],
                          telefono=persona['telefono'],
                          tipo=persona['tipo'],
                          estado=persona['estado'], 
                          foto=persona['foto'], 
                          fecha=persona['fecha'], 
                          codigo=persona['codigo']).model_dump()
        return {"ok": persona}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Problemas con la base de datos")

def get_all(skip: int = 0, limit: int = 100):
    if validar_coneccion_db():
        rows = repository.get_all(skip, limit)
        lista = [Persona(idpersona=data['idpersona'], 
                          idusuario=data['idusuario'], 
                          nombres=data['nombres'], 
                          apellidos=data['apellidos'],
                          direccion=data['direccion'],
                          telefono=data['telefono'],
                          tipo=data['tipo'],
                          estado=data['estado'], 
                          foto=data['foto'], 
                          fecha=data['fecha'], 
                          codigo=data['codigo']).model_dump() for data in rows] if rows else []  
        return {'ok': lista}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Problemas con la base de datos")
    


