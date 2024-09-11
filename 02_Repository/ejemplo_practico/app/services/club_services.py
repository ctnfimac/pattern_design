from sqlalchemy.orm import Session
from repositories.club_repository import ClubRepository
from models.club import Club
from schemas.club_schema import ClubCreate

class ClubService:

    def __init__(self, db: Session):
        self.club_repository = ClubRepository(db)

    def obtener_clubes(self) -> list[Club]:
        return self.club_repository.get_clubes()
    
    def crear_club(self, club: ClubCreate) -> Club:
        return self.club_repository.post_club(club)