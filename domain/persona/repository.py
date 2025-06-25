from .schemas import PersonaCreate, Persona
import utils.conection_db as conn
from fastapi.responses import JSONResponse
import json

def validar_coneccion():
    conn.db.open()
    conn.db.cursor.execute("select now()")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def get_all(skip: int = 0, limit: int = 100):

    conn.db.open()
    conn.db.cursor.execute("SELECT * FROM persona where estado='A'")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def find_by_codigo(codigo: str):
    conn.db.open()
    query = f"SELECT idpersona, idusuario, nombres, apellidos, direccion, telefono, tipo, estado, fecha, codigo FROM persona WHERE codigo = '{codigo}' and estado='A'"
    conn.db.cursor.execute(query)
    found = conn.db.cursor.fetchone()
    conn.db.close()
    return found

def add(data: PersonaCreate):
    query = "insert into persona (nombres, apellidos, direccion, telefono, codigo) values (%s, %s, %s, %s, %s)"
    conn.db.open()
    conn.db.cursor.execute(query, (data.nombres,
                                   data.apellidos,
                                   data.direccion,
                                   data.telefono,
                                   data.codigo))
    conn.db.session.commit()
    personid = conn.db.cursor.lastrowid
    
    query = f"SELECT idpersona, idusuario, nombres, apellidos, direccion, telefono, tipo, foto, estado, fecha, codigo FROM persona WHERE idpersona = '{personid}'"
    conn.db.cursor.execute(query)
    found = conn.db.cursor.fetchone()
    conn.db.close()
    return found
    