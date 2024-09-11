from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base


class Club(Base):

    __tablename__ = 'clubes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, index=True)
    capacidad = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    jugadores = relationship("Jugador", back_populates="owner_club")