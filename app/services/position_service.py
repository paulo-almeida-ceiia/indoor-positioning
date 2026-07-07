from sqlalchemy.orm import Session

from app.db.models import Position


def save_position(
    db: Session,
    tag_id: int,
    x: float,
    y: float,
    z: float,
):
    position = Position(
        tag_id=tag_id,
        x=x,
        y=y,
        z=z,
    )

    db.add(position)
    db.commit()
    db.refresh(position)

    return position
