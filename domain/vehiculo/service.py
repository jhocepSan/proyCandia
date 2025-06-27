from fastapi import HTTPException, status
from utils.exceptions import DuplicatedError, DatabaseError, ErrorGeneral
from . import repository
from .schemas import Vehiculo, VehiculoCreate, TipoVehiculo, VehiculoUpdate

def validar_coneccion_db():
    try:
        result = repository.validar_coneccion()
        return True
    except Exception as error:
        return False

def crear_vehiculo(data: VehiculoCreate) -> Vehiculo:
    if validar_coneccion_db():
        found = repository.find_by_placa(data.placa)
        if found:
            raise DuplicatedError(detail="El vehiculo ya existe")
        tipo_vehiculo =handle_tipovehiculo(data.tipoId, data.tipoNombre)
        data.tipoId = tipo_vehiculo.id if tipo_vehiculo else None

        vehiculo = repository.add(data)
        vehiculo = Vehiculo(id=vehiculo['idvehiculo'], 
                          modelo=vehiculo['modelo'], 
                          placa=vehiculo['placa'], 
                          color=vehiculo['color'],
                          tipo=tipo_vehiculo,
                          motor=vehiculo['motor'],
                          km=vehiculo['km'],
                          fotoplaca=vehiculo['fotoplaca'], 
                          foto=vehiculo['foto'], 
                          fecha=vehiculo['fecha']).model_dump()
        return vehiculo
    else:
        raise DatabaseError(detail="Problemas con la base de datos")

def get_all(skip: int = 0, limit: int = 100):
    if validar_coneccion_db():
        rows = repository.get_all(skip, limit)
        res = []
        for data in rows:
            tipoVehiculo = None
            if data['idtipo'] and data['idtipo'] > 0:
                tipoVehiculo = repository.get_tipoVehiculo_byId(data['idtipo'])
                tipoVehiculo = TipoVehiculo(id=tipoVehiculo['idtipovehiculo'], nombre=tipoVehiculo['nombre'], estado=tipoVehiculo['estado'])
            res.append(Vehiculo(id=data['idvehiculo'], 
                          modelo=data['modelo'], 
                          placa=data['placa'], 
                          color=data['color'],
                          tipo=tipoVehiculo,
                          motor=data['motor'],
                          km=data['km'],
                          fotoplaca=data['fotoplaca'], 
                          foto=data['foto'], 
                          fecha=data['fecha']).model_dump())
        
        return res
    else:
        raise DatabaseError(detail="Problemas con la base de datos")

def get_tipoVehiculos():
    if validar_coneccion_db():
        rows = repository.get_tipoVehiculos()
        lista = [TipoVehiculo(id=data['idtipovehiculo'], nombre=data['nombre'], estado=data['estado']).model_dump() for data in rows] if rows else []  
        return lista
    else:
        raise DatabaseError(detail="Problemas con la base de datos")
def handle_tipovehiculo(tipo_id: int=None, nombre: str=None) -> TipoVehiculo|None:
    res = None
    if nombre and (tipo_id == 0 or tipo_id is None):
        res = repository.add_tipoVehiculo(nombre)
    if tipo_id and tipo_id > 0:
        res = repository.get_tipoVehiculo_byId(tipo_id)
    if res:
        res = TipoVehiculo(id=res['idtipovehiculo'], nombre=res['nombre'],
                                    estado=res['estado'])
    return res

def update_vehiculo(vehiculo: VehiculoUpdate) -> bool:
    if validar_coneccion_db():
        found = repository.find_by_placa(vehiculo.placa)
        if found and vehiculo.id != found['idvehiculo']:
            raise DuplicatedError(detail="El vehiculo con la placa proporcionada ya existe")
        tipo_vehiculo =handle_tipovehiculo(vehiculo.tipoId, vehiculo.tipoNombre)
        vehiculo.tipoId = tipo_vehiculo.id if tipo_vehiculo else None
        res = repository.update(vehiculo)
        if res == False:
            raise 
    else:
        raise DatabaseError(detail="Problemas con la base de datos")

