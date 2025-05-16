from .schemas import UsuarioCreate, Usuario
import utils.conection_db as conn
from fastapi.responses import JSONResponse
import json


def get_all(skip: int = 0, limit: int = 100):

    conn.db.open()
    conn.db.cursor.execute("SELECT * FROM usuario")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def findByUsernameEmail(username: str, email: str):
    conn.db.open()
    select = "SELECT idusuario, nameusuario, tipo, correo, usoapp, contrasenia FROM usuario WHERE"
    byName = f"{select} nameusuario = '{username}'"
    byEmail = f"{select} correo = '{email}'"
    conn.db.cursor.execute(byName)
    found = conn.db.cursor.fetchone()
    if found is None:
        conn.db.cursor.execute(byEmail)
        found = conn.db.cursor.fetchone()
    conn.db.close()
    return found

def add(usuario: UsuarioCreate):
    conn.db.open()
    conn.db.cursor.execute("INSERT INTO usuario (nameusuario, correo, tipo, usoapp, contrasenia) VALUES (%s, %s, %s, %s, %s)", 
                           (usuario.nombre,
                            usuario.correo,
                            usuario.tipo,
                            usuario.app,
                            usuario.contrasenia))
    conn.db.session.commit()
    conn.db.close()
