from fastapi import HTTPException
from sqlalchemy.orm import Session
from mysql.connector import Error
from schemas.jugador_schema import JugadorCreate


class JugadorRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_jugadores(self, skip:int, limit:int):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, dni, owner_club_id FROM jugadores")
        resultado = cursor.fetchall()
        return resultado
    
    
    def create_jugador(self, jugador: JugadorCreate, club_id: int):
        try:
            cursor = self.db.cursor()
            cursor.execute(
                """INSERT INTO jugadores(nombre, dni, owner_club_id)
                VALUES(%s, %s, %s);""",
                (jugador.nombre, jugador.dni, club_id)
            )
            self.db.commit()
            id = cursor.lastrowid
            return {"id": id, "nombre": jugador.nombre, "dni" : jugador.dni, "owner_club_id": club_id}
        
        except Error as e:
            print(f"Error al insertar los datos: {e}")
            raise HTTPException(status_code=500, detail="Error al insertar los datos")
    