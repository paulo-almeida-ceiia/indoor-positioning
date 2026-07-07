from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.anchor import AnchorUpdate

from app.db.database import get_db
from app.db.models import Anchor
from app.schemas.anchor import AnchorCreate, AnchorResponse

router = APIRouter(prefix="/anchors", tags=["Anchors"])


@router.post("/", response_model=AnchorResponse)
def create_anchor(anchor: AnchorCreate, db: Session = Depends(get_db)):
    db_anchor = Anchor(**anchor.model_dump())

    db.add(db_anchor)
    db.commit()
    db.refresh(db_anchor)

    return db_anchor


@router.get("/", response_model=list[AnchorResponse])
def get_anchors(db: Session = Depends(get_db)):
    return db.query(Anchor).all()

@router.get("/{anchor_id}", response_model=AnchorResponse)
def get_anchor(anchor_id: int, db: Session = Depends(get_db)):
    anchor = db.query(Anchor).filter(Anchor.id == anchor_id).first()

    if anchor is None:
        raise HTTPException(
            status_code=404,
            detail="Anchor not found"
        )

    return anchor

@router.put("/{anchor_id}", response_model=AnchorResponse)
def update_anchor(
    anchor_id: int,
    anchor_data: AnchorUpdate,
    db: Session = Depends(get_db)
):
    anchor = db.query(Anchor).filter(Anchor.id == anchor_id).first()

    if anchor is None:
        raise HTTPException(
            status_code=404,
            detail="Anchor not found"
        )

    updates = anchor_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(anchor, key, value)

    db.commit()
    db.refresh(anchor)

    return anchor

@router.delete("/{anchor_id}")
def delete_anchor(
    anchor_id: int,
    db: Session = Depends(get_db)
):
    anchor = db.query(Anchor).filter(Anchor.id == anchor_id).first()

    if anchor is None:
        raise HTTPException(
            status_code=404,
            detail="Anchor not found"
        )

    db.delete(anchor)
    db.commit()

    return {
        "message": "Anchor deleted successfully"
    }

