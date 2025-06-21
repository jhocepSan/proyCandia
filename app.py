import os,uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import usuario, auth, persona
import utils.conection_db as conection_db
import utils.api_logger as apiLogger
import utils.api_telegram as apiTelegram

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
apiTelegram.init()
apiLogger.init()
conection_db.init()

app.include_router(persona.router)
app.include_router(usuario.router)
app.include_router(auth.router)

#para crear el ejecutable del servidor
'''
def server():
    uvicorn.run(app, port=4001, host="0.0.0.0",access_log=True)

if __name__ == "__main__":
    server()
'''