from .schemas import UsuarioCreate, Usuario,UpdateUser,ChangeEstadoUser
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
    conn.db.cursor.execute("""SELECT idusuario,nameusuario,correo,estado,tipo,usoapp,
        (case when estado='A' then 'ACTIVO' when estado='I' then 'INACTIVO'
        when estado='E' then 'ELIMINADO' END) as name_estado,
        (case when tipo='A' then 'ADMINISTRADOR' when tipo='U' then 'USUARIO NORMAL'
        when tipo='C' then 'CLIENTE' else 'OTRO' end) as name_tipo,
        (case when usoapp='D' then 'USO ESCRITORIO' when usoapp='A' then 'USO CELULAR'
        when usoapp='W' then 'USO WEB' else 'OTRO' end)as name_usoapp
        FROM usuario where estado !='E';""")
    res = conn.db.cursor.fetchall()
    conn.db.close()
    return res

def findByUsernameEmail(username: str, email: str):
    conn.db.open()
    select = "SELECT idusuario, nameusuario, tipo, correo, usoapp, contrasenia FROM usuario WHERE estado='A' and"
    byName = f"{select} nameusuario = '{username}'"
    byEmail = f"{select} correo = '{email}'"
    conn.db.cursor.execute(byName)
    found = conn.db.cursor.fetchone()
    if found is None:
        conn.db.cursor.execute(byEmail)
        found = conn.db.cursor.fetchone()
    conn.db.close()
    return found
def changePasswordUser(datos):
    sql = "update usuario set contrasenia=%s where idusuario=%s"
    conn.db.open()
    conn.db.cursor.execute(sql,(datos['contrasenia'],datos['id']))
    conn.db.session.commit()
    if conn.db.cursor.rowcount > 0 :
        conn.db.close()
        return True
    else:
        conn.db.close()
        return False
def updateUser(usuario: UpdateUser):
    conn.db.open()
    conn.db.cursor.execute("UPDATE usuario set nameusuario=%s,correo=%s,tipo=%s,usoapp=%s where idusuario=%s",
                           (usuario.nombre,usuario.correo,usuario.tipo,usuario.app,usuario.id))
    conn.db.session.commit()
    if conn.db.cursor.rowcount > 0 :
        conn.db.close()
        return True
    else:
        conn.db.close()
        return False

def cahnge_estado_user(usuario:ChangeEstadoUser):
    conn.db.open()
    conn.db.cursor.execute("UPDATE usuario set estado=%s where idusuario=%s",(usuario.estado,usuario.id))
    conn.db.session.commit()
    if conn.db.cursor.rowcount > 0 :
        conn.db.close()
        return True
    else:
        conn.db.close()
        return False
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
