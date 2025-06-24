from mysql.connector import pooling
import json

class ApiResponse:
    def __init__(self, ok=None, error=None):
        self.ok = ok,
        self.error = error,
