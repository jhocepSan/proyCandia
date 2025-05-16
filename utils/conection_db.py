from mysql.connector import pooling
import json

class ConexionDB:
    def __init__(self,**config):
        self.connection_pool = pooling.MySQLConnectionPool(
            pool_name=config['POOL_NAME'],
            pool_size=config['POOL_SIZE'],
            pool_reset_session=True,
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            database=config['DATABASE'],
            port=config['PORT']
        )
        self.session = None
        self.cursor = None

    def open(self):
        self.session = self.connection_pool.get_connection()
        self.cursor = self.session.cursor(dictionary=True)

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.session is not None:
            self.session.close()

def init():
    try:
        global db
        with open("./config/config.json","r") as f:
            config = json.load(f)
        db = ConexionDB(**config['DB_CONFIG'])
    except Exception as e:
        print(e)
