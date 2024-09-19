from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.jugador import Jugador
from models.club import Club
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
        pass
    