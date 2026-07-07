from pydantic import BaseModel, ConfigDict


class AnchorBase(BaseModel):
    name: str
    x: float
    y: float
    z: float
    online: bool = True


class AnchorCreate(AnchorBase):
    pass


class AnchorUpdate(BaseModel):
    name: str | None = None
    x: float | None = None
    y: float | None = None
    z: float | None = None
    online: bool | None = None


class AnchorResponse(AnchorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
