from fastapi import FastAPI

from app.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
