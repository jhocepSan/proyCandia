from psycopg2 import pool
import json

class ConexionDB:
    def __init__(self,min_conection,max_conection,**config):
        self.conection_pool = pool.SimpleConnectionPool(
            minconn=min_conection,
            maxconn=max_conection,
            **config)
    def get_connection(self):
        return self.conection_pool.getconn()
    def return_connection(self,conection):
        self.conection_pool.putconn(conection)
    def close_pool(self):
        self.conection_pool.closeall()

def init():
    try:
        with open("config.json","r") as f:
            config = json.load(f)
            return ConexionDB(**config)
    except Exception as e:
        print(e)
