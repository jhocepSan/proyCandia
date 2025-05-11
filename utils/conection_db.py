import mysql.connector
from mysql.connector import pooling
import json

class ConexionDB:
    def __init__(self,**config):
        self.conection_pool = pooling.MySQLConnectionPool(
            pool_name=config['POOL_NAME'],
            pool_size=config['POOL_SIZE'],
            pool_reset_session=True,
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            database=config['DATABASE'],
            port=config['PORT']
        )
    def get_connection(self):
        return self.conection_pool.get_connection()

def init():
    try:
        with open("config.json","r") as f:
            config = json.load(f)
            return ConexionDB(**config['DB_CONFIG'])
    except Exception as e:
        print(e)
