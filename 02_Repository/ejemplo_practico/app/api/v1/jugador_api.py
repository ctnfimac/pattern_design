from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from db.base import get_db
from services.jugador_services import JugadorServices
from schemas.jugador_schema import JugadorRequest
from schemas.jugador_schema import JugadorCreate


router_jugador_api = APIRouter()

@router_jugador_api.get("/jugadores/", response_model=list[JugadorRequest])
def read_jugadores(db: Session = Depends(get_db)):
    jugador_services = JugadorServices(db)
    return jugador_services.obtener_jugadores()



@router_jugador_api.post("/jugadores/", response_model=JugadorRequest)
async def crear_jugador(jugador: JugadorCreate, db: Session = Depends(get_db)):
    jugador_services = JugadorServices(db)
    return jugador_services.crear_jugador(jugador=jugador)