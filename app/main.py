from contextlib import asynccontextmanager
import threading

from fastapi import FastAPI

from app.db.database import engine, Base
import app.db.models

from app.api.anchors import router as anchor_router
from app.api.tags import router as tag_router
from app.api.positions import router as position_router

from app.uwb.pipeline import run


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    print("Starting UWB pipeline...")

    thread = threading.Thread(target=run, daemon=True)

    thread.start()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(anchor_router)
app.include_router(tag_router)
app.include_router(position_router)
