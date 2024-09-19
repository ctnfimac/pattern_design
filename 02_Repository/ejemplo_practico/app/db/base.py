from fastapi import FastAPI, HTTPException
import mysql.connector
from mysql.connector import Error

def session_local():
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            database='02repository',
            user='root',
            password=''
        )
        if connection.is_connected():
            return connection
    except Error as e:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
