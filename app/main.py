from fastapi import FastAPI

from app.database import engine,Base
from app.models import *
from app.routers import router

Base.metadata.create_all(engine)

app = FastAPI(title='Books Api')

app.include_router(router)