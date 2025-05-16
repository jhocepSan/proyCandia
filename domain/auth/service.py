from typing import Tuple
from fastapi import HTTPException
from datetime import datetime, timedelta
import bcrypt
from jose import jwt
from domain.usuario import repository as userRepository
from utils.exceptions import AuthError
from .schemas import SignIn
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
            return token
        else:
            raise AuthError(detail="Credenciales Invalidos")


