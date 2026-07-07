from pydantic import BaseModel
from datetime import datetime


class Measurement(BaseModel):

    tag_id: int

    distances: dict[int, float]

    timestamp: datetime