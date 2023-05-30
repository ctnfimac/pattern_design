import os
import sqlite3

class Database:
    _db_name: str = 'test.db'
    _db_folder: str = 'db'
    _path_db: str = None
    cur: None

    
    def __init__(self):
        self._path_db = f'{os.getcwd()}/{self._db_folder}/{self._db_name}'
        
    def connect(self):
        con = sqlite3.connect(self._path_db)
        self.cur = con.cursor()

    def disconnect(self):
        self.cur.close()

        