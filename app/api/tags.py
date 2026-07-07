from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Tag
from app.schemas.tag import TagCreate, TagUpdate, TagResponse

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=TagResponse)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = Tag(**tag.model_dump())

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


@router.get("/", response_model=list[TagResponse])
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag


@router.put("/{tag_id}", response_model=TagResponse)
def update_tag(tag_id: int, tag_data: TagUpdate, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    updates = tag_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(tag, key, value)

    db.commit()
    db.refresh(tag)

    return tag


@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    db.delete(tag)
    db.commit()

    return {"message": "Tag deleted successfully"}
