#hier alles ausführen

from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()           #import and instantiate the FastAPI

@app.on_event("startup")  #register the root endpoint / which then returns a JSON
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])        #register routes file in main.py
                                                                            # added prefix /api/v1/movies so, that managing different version of API becomes easier. 
                                                                            # Also, tags make finding API related to movies easier in FastAPI docs


