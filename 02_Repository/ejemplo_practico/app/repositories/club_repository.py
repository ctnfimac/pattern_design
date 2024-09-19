from sqlalchemy.orm import Session
from models.club import Club
from schemas.club_schema import ClubCreate


class ClubRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_clubes(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT nombre, capacidad FROM clubes")
        resultado = cursor.fetchall()
        return resultado
    
    def post_club(self, club: ClubCreate):
        pass