import uvicorn
from fastapi import FastAPI
from api.v1.jugador_api import router_jugador_api
from api.v1.club_api import router_club_api


app = FastAPI()

app.include_router(router_jugador_api)
app.include_router(router_club_api)


if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", reload=True)

