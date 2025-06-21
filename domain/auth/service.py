from typing import Tuple
from fastapi import HTTPException
from datetime import datetime, timedelta
import bcrypt
import jwt
from domain.usuario import repository as userRepository
from utils.exceptions import AuthError,DatabaseError,ErrorGeneral
from .schemas import SignIn,SingInChangePassword
import json

def create_access_token(subject: dict, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        with open("./config/config.json","r") as f:
            confT = json.load(f)
        expire = datetime.utcnow() + timedelta(minutes=confT['ACCESS_TOKEN_EXPIRE_MINUTES'])
    payload = {"exp": expire, **subject}
    encoded_jwt = jwt.encode(payload, '', algorithm='HS256')
    return encoded_jwt

def sign_in(cred: SignIn):
    find_user = userRepository.findByUsernameEmail(cred.usuario, cred.usuario)    
    if find_user and bcrypt.checkpw(cred.contrasena.encode('utf-8'), find_user['contrasenia'].encode('utf-8')):
        token = create_access_token({'id': find_user['idusuario'], 'nombre': cred.usuario})
        return {'ok':token}
    else:
        raise AuthError(detail="Credenciales Invalidos")

def change_pass(user_info:SingInChangePassword):
    print(user_info.correo,user_info.newcontrasenia,user_info.contrasenia)
    try:
        if userRepository.validar_coneccion():
            find_user = userRepository.findByUsernameEmail('',user_info.correo)
            if find_user and find_user['idusuario']==user_info.id :
                if bcrypt.checkpw(user_info.contrasenia.encode('utf-8'),find_user['contrasenia'].encode('utf-8')):
                    hashed_password = bcrypt.hashpw(user_info.newcontrasenia.encode('utf-8'), bcrypt.gensalt())
                    if userRepository.changePasswordUser({'id':find_user['idusuario'],'contrasenia':hashed_password}):
                        return {'ok':'Cambio correcto'}
                    else:
                        raise ErrorGeneral(detail="Algo salio mal, reintente nuevamente")
            raise ErrorGeneral(detail="Datos incorrectos...")
        else:
            raise DatabaseError(detail="Problemas con la base de datos")
    except Exception as error:
        raise ErrorGeneral(detail=str(error))