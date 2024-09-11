from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.base import Base

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    dni = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    owner_club_id = Column(Integer, ForeignKey("clubes.id"))
    owner_club = relationship("Club", back_populates="jugadores")
    