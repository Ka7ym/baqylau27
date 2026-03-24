from pydantic import BaseModel
from uuid import UUID


class GymRead(BaseModel):
    id: UUID
    plant_name: str
    harvest_year: int
    farm_id: UUID

    class Config:
        from_attributes = True


class GymCreate(BaseModel):
    plant_name: str
    harvest_year: int
    farm_id: UUID

    class Config:
        from_attributes = True