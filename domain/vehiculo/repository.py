from .schemas import Vehiculo, VehiculoCreate, VehiculoUpdate
import utils.conection_db as conn
from fastapi.responses import JSONResponse

def validar_coneccion():
    conn.db.open()
    conn.db.cursor.execute("select now()")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def get_all(skip: int = 0, limit: int = 100):
    conn.db.open()
    conn.db.cursor.execute("SELECT * FROM vehiculo")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def get_tipoVehiculos():
    """recupera tipo de vehiculos activos"""
    conn.db.open()
    conn.db.cursor.execute("SELECT * FROM tipovehiculo WHERE estado='A'")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def get_tipoVehiculo_byId(id: int):
    conn.db.open()
    conn.db.cursor.execute(f"SELECT * FROM tipovehiculo where idtipovehiculo={id}")
    res = conn.db.cursor.fetchone()
    conn.db.close()
    return res

def find_by_placa(placa: str):
    conn.db.open()
    query = f"SELECT idvehiculo, modelo, placa, color, fecha, idtipo, motor, km, fotoplaca, foto FROM vehiculo WHERE placa = '{placa}'"
    conn.db.cursor.execute(query)
    found = conn.db.cursor.fetchone()
    conn.db.close()
    return found

def add(data: VehiculoCreate):
    query = "insert into vehiculo (modelo, placa, color, idtipo, motor, km, fotoplaca, foto) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn.db.open()
    conn.db.cursor.execute(query, (data.modelo, data.placa, data.color, data.tipoId, data.motor, data.km, data.fotoplaca, data.foto))
    conn.db.session.commit()
    vehiculoid = conn.db.cursor.lastrowid
    
    query = f"SELECT idvehiculo, modelo, placa, color, idtipo, motor, km, fotoplaca, foto, fecha FROM vehiculo WHERE idvehiculo = '{vehiculoid}'"
    conn.db.cursor.execute(query)
    found = conn.db.cursor.fetchone()
    conn.db.close()
    return found

def add_tipoVehiculo(data):
    query = "insert into tipovehiculo (nombre) values (%s)"
    conn.db.open()
    conn.db.cursor.execute(query, (data,))
    conn.db.session.commit()
    idtipo = conn.db.cursor.lastrowid
    
    query = f"SELECT idtipovehiculo, nombre, estado FROM tipovehiculo WHERE idtipovehiculo = '{idtipo}'"
    conn.db.cursor.execute(query)
    found = conn.db.cursor.fetchone()
    conn.db.close()
    return found

def update(vehiculo: VehiculoUpdate):
    conn.db.open()
    query = f"update vehiculo set modelo=%s, placa=%s, color=%s, idtipo=%s, motor=%s, km=%s, fotoplaca=%s, foto=%s where idvehiculo={vehiculo.id}"
    conn.db.cursor.execute(query,
                           (vehiculo.modelo, vehiculo.placa, vehiculo.color, vehiculo.tipoId, vehiculo.motor, vehiculo.km, vehiculo.fotoplaca, vehiculo.foto))
    conn.db.session.commit()
    res = True if conn.db.cursor.rowcount > 0 else False
    conn.db.close()
    return res
