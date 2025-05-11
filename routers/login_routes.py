from fastapi import APIRouter,Request
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/usuario',
    tags=['usuario']
)

@router.post("/singin")
async def iniciar_session(request: Request):
    try:
        data = await request.json()
        return JSONResponse(status_code=200, content={"message": "ok"})
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": f"Error: {e}"})
