from pydantic import BaseModel


class JugadorCreate(BaseModel):
    """Validaciones de entrada"""
    nombre: str
    dni: str

    #class Config:
    #    orm_mode = True


class JugadorRequest(BaseModel):
    """Validaciones de salida"""
    id: int
    nombre: str
    owner_club_id: int

    class Config:
        orm_mode = True