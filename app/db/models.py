from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from .database import Base


class Anchor(Base):
    __tablename__ = "anchors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    x: Mapped[float]
    y: Mapped[float]
    z: Mapped[float]
    status: Mapped[str] = mapped_column(String(20))


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    asset_name: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20))
    battery: Mapped[int]


class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True)

    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))

    x: Mapped[float]
    y: Mapped[float]
    z: Mapped[float]

    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
