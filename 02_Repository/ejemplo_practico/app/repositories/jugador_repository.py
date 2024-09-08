from sqlalchemy.orm import Session
from models.jugador import Jugador
from schemas.jugador_schema import JugadorCreate


class JugadorRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_jugadores(self, skip:int, limit:int):
        return self.db.query(Jugador).offset(skip).limit(limit).all()
    
    
    def create_jugador(self, jugador: JugadorCreate):
        jugador_nuevo = Jugador(
            nombre=jugador.nombre, 
            dni=jugador.dni
        )
        self.db.add(jugador_nuevo)
        self.db.commit()
        self.db.refresh(jugador_nuevo)
        return jugador_nuevo
    