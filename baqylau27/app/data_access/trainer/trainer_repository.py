from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from data_access.db.models.trainer import Trainer

class TrainerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Trainer]:
        result = await self.db.execute(select(Trainer))
        return result.scalars().all()
    
    async def get_by_id(self, trainer_id: UUID) -> Trainer | None:
        result = await self.db.execute(select(Trainer).where(Trainer.id == trainer_id))
        return result.scalar_one_or_none()
    
    async def create(self, trainer: Trainer) -> Trainer:
        self.db.add(trainer)
        await self.db.commit()
        await self.db.refresh(trainer)

        return trainer