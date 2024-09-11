from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from db.base import get_db
from schemas.club_schema import ClubResponse
from schemas.club_schema import ClubCreate
from services.club_services import ClubService


router_club_api = APIRouter()


@router_club_api.get('/clubes/', response_model=list[ClubResponse])
def listar_clubes(db: Session=Depends(get_db)):
    club_service = ClubService(db)
    return club_service.obtener_clubes()



@router_club_api.post('/clubes/', response_model=ClubResponse)
async def crear_club(club: ClubCreate,  db: Session=Depends(get_db)):
    club_service = ClubService(db)
    return club_service.crear_club(club)