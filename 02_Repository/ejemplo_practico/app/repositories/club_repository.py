from sqlalchemy.orm import Session
from models.club import Club
from schemas.club_schema import ClubCreate


class ClubRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_clubes(self):
        return self.db.query(Club).all()
    
    def post_club(self, club: ClubCreate):
        club_nuevo = Club(
            nombre = club.nombre,
            capacidad = club.capacidad
        )
        self.db.add(club_nuevo)
        self.db.commit()
        self.db.refresh(club_nuevo)
        return club_nuevo