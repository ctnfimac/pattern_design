from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.jugador import Jugador
from models.club import Club
from schemas.jugador_schema import JugadorCreate


class JugadorRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_jugadores(self, skip:int, limit:int):
        return self.db.query(Jugador).offset(skip).limit(limit).all()
    
    
    def create_jugador(self, jugador: JugadorCreate, club_id: int):
        club = self.db.query(Club).filter(Club.id == club_id).first()

        if not club:
            raise HTTPException(status_code=404, detail="Club no existente")

        jugador_nuevo = Jugador(
            nombre=jugador.nombre, 
            dni=jugador.dni,
            owner_club_id = club_id
        )
        self.db.add(jugador_nuevo)
        self.db.commit()
        self.db.refresh(jugador_nuevo)
        return jugador_nuevo
    