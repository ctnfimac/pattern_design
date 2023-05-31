import os
import sqlite3

class Database:
    _db_name: str = 'test.db'
    _db_folder: str = 'db'
    _path_db: str = None
    cur: None
    conexion: None

    
    def __init__(self):
        self._path_db = f'{os.getcwd()}/{self._db_folder}/{self._db_name}'
        
    def connect(self):
        self.conexion = sqlite3.connect(self._path_db)
        self.cur = self.conexion.cursor()

    def disconnect(self):
        self.cur.close()

        