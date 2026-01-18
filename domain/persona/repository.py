from .schemas import PersonaCreate, Persona,ChangeEstadoPerson
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
    conn.db.cursor.execute("SELECT * FROM persona where estado<>'E'")
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

def change_estado_persona(data:ChangeEstadoPerson):
    try:
        query = "update persona set estado=%s where idpersona=%s"
        conn.db.open()
        conn.db.cursor.execute(query,(data.estado,data.idpersona))
        conn.db.session.commit()
        if conn.db.cursor.rowcount > 0 :
            conn.db.close()
            return {'ok':'Actualizacion de estado Correcto'}
        else:
            conn.db.close()
            return {'error':"No se cambio el estado del cliente"}
    except Exception as error:
        print(error)
        return {'error':str(error)}
    