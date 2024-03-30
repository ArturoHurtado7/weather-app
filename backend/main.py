import uvicorn

from fastapi import FastAPI
from config import APP_PORT

from src import models
from src.router import router
from src.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router, tags=["Weather API"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(APP_PORT))
