from pydantic import BaseModel
from schemas.jugador_schema import JugadorRequest


class ClubCreate(BaseModel):
    nombre: str
    capacidad: int

    #class Config:
    #    orm_mode = True



class ClubResponse(BaseModel):
    nombre: str
    capacidad: int
    #jugadores: list[JugadorRequest] = []

    #class Config:
    #    orm_mode = True