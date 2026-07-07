from pydantic import BaseModel, ConfigDict


class TagBase(BaseModel):
    name: str
    active: bool = True


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    name: str | None = None
    active: bool | None = None


class TagResponse(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
