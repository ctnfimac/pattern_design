from fastapi import HTTPException
from sqlalchemy.orm import Session
from mysql.connector import Error
from schemas.club_schema import ClubCreate


class ClubRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_clubes(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT nombre, capacidad FROM clubes")
        resultado = cursor.fetchall()
        return resultado
    
    def post_club(self, club: ClubCreate):
        try:
            cursor = self.db.cursor()
            cursor.execute(
                """INSERT INTO clubes(nombre, capacidad)
                VALUES(%s, %s);""",
                (club.nombre, club.capacidad)
            )
            self.db.commit()

            return {"nombre": club.nombre, "capacidad" : club.capacidad}
        except Error as e:
            print(f"Error al insertar los datos: {e}")
            raise HTTPException(status_code=500, detail="Error al insertar los datos")