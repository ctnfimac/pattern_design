import uvicorn
from fastapi import FastAPI
from db.base import Base
from db.base import engine
from api.v1.jugador_api import router_jugador_api


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router_jugador_api)


if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", reload=True)

