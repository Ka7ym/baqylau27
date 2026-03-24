from fastapi import HTTPException
from data_access.trainer.trainer_repository import Trainer
from data_access.db.models.trainer import Trainer
from api.trainer.trainer_schemas import TrainerRead, TrainerCreate

from uuid import UUID

class TrainerService:
    def __init__(self, repo: Trainer):
        self.repo = repo

    async def get_trainer(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, trainer_id: UUID):
        trainer = await self.repo.get_by_id(trainer_id)

        if not trainer:
            raise HTTPException(status_code=404, detail="Trainer not found")
        return trainer
    
    async def create(self, data: TrainerCreate):
        trainer = Trainer(
            name=data.name,
            country=data.country,
            iata_code=data.iata_code
        )

        return await self.repo.create(trainer)