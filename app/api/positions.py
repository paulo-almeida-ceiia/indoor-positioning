from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Position, Tag
from app.schemas.position import (
    PositionCreate,
    PositionUpdate,
    PositionResponse,
)

router = APIRouter(prefix="/positions", tags=["Positions"])


@router.post("/", response_model=PositionResponse)
def create_position(position: PositionCreate, db: Session = Depends(get_db)):
    # Check if the tag exists
    tag = db.query(Tag).filter(Tag.id == position.tag_id).first()

    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    # Create the position
    db_position = Position(**position.model_dump())

    db.add(db_position)
    db.commit()
    db.refresh(db_position)

    return db_position


@router.get("/", response_model=list[PositionResponse])
def get_positions(db: Session = Depends(get_db)):
    return db.query(Position).all()


@router.get("/{position_id}", response_model=PositionResponse)
def get_position(position_id: int, db: Session = Depends(get_db)):
    position = db.query(Position).filter(Position.id == position_id).first()

    if position is None:
        raise HTTPException(status_code=404, detail="Position not found")

    return position


@router.put("/{position_id}", response_model=PositionResponse)
def update_position(
    position_id: int, position_data: PositionUpdate, db: Session = Depends(get_db)
):
    position = db.query(Position).filter(Position.id == position_id).first()

    if position is None:
        raise HTTPException(status_code=404, detail="Position not found")

    updates = position_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(position, key, value)

    db.commit()
    db.refresh(position)

    return position


@router.delete("/{position_id}")
def delete_position(position_id: int, db: Session = Depends(get_db)):
    position = db.query(Position).filter(Position.id == position_id).first()

    if position is None:
        raise HTTPException(status_code=404, detail="Position not found")

    db.delete(position)
    db.commit()

    return {"message": "Position deleted successfully"}
