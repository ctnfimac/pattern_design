from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.base import Base

class Jugador(Base):
    __tablename__ = "jugador"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    dni = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())