from pydantic import BaseModel
from uuid import UUID


class TrainerRead(BaseModel):
    id: UUID
    name: str
    region: str
    area_hectares: float

    class Config:
        from_attributes = True


class TrainerCreate(BaseModel):
    name: str
    region: str
    area_hectares: float

    class Config:
        from_attributes = True