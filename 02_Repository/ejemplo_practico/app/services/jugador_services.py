from repositories.jugador_repository import JugadorRepository
from models.jugador import Jugador
from sqlalchemy.orm import Session
from schemas.jugador_schema import JugadorCreate


class JugadorServices:
    
    def __init__(self, db: Session):
        self.jugador_repository = JugadorRepository(db)

    def obtener_jugadores(self, skip: int = 0, limit: int = 100) -> list[Jugador]:
        return self.jugador_repository.get_jugadores(skip, limit)
    
    def crear_jugador(self, jugador: JugadorCreate, club_id: int):
        return self.jugador_repository.create_jugador(jugador, club_id)
    