from fastapi import APIRouter,Request
from fastapi.responses import JSONResponse
from utils import api_logger,api_telegram
import utils.conection_db as conection_db
import json

router = APIRouter(
    prefix='/usuario',
    tags=['usuario']
)

@router.post("/singin")
async def iniciar_session(request: Request):
    try:
        data = await request.json()
        return JSONResponse(status_code=200, content={"ok": "ok"})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"Error: {e}"})
    
@router.get("/getUsuarios")
async def get_usuarios(request: Request):
    conn=None
    cursor=None
    try:
        conn = conection_db.conectionDb.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario")
        rows = cursor.fetchall()
        json_resultado = json.dumps(rows, ensure_ascii=False)
        return JSONResponse(status_code=200, content={"ok": json_resultado})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"Error: {e}"})
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
