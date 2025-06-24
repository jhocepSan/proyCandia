from fastapi import HTTPException, status
from utils.exceptions import DuplicatedError, DatabaseError
from . import repository
from .schemas import Vehiculo, VehiculoCreate, TipoVehiculo
from utils.ApiResponse import ApiResponse

def validar_coneccion_db():
    try:
        result = repository.validar_coneccion()
        return True
    except Exception as error:
        return False

def crear_vehiculo(data: VehiculoCreate) -> Vehiculo:
    if validar_coneccion_db():
        tipoVehiculo = None
        data.tipoId = None
        found = repository.find_by_placa(data.placa)
        if found:
            raise DuplicatedError(detail="El vehiculo ya existe")
        if data.tipoNombre and (data.tipoId == 0 or data.tipoId == None):
            tipoVehiculo = repository.add_tipoVehiculo(data.tipoNombre)
            tipoVehiculo = TipoVehiculo(id=tipoVehiculo['idtipovehiculo'], nombre=tipoVehiculo['nombre'], estado=tipoVehiculo['estado'])
            data.tipoId = tipoVehiculo.id

        vehiculo = repository.add(data)
        vehiculo = Vehiculo(id=vehiculo['idvehiculo'], 
                          modelo=vehiculo['modelo'], 
                          placa=vehiculo['placa'], 
                          color=vehiculo['color'],
                          tipo=tipoVehiculo,
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
