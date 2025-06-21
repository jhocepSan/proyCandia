from domain.auth import service
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from utils import api_logger,api_telegram
from domain.auth.schemas import SignIn,SingInChangePassword

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post("/signin")
async def sign_in(user_info: SignIn):
    return service.sign_in(user_info)

@router.post("/changepass")
async def change_pass(user_info:SingInChangePassword):
    return service.change_pass(user_info)

    
