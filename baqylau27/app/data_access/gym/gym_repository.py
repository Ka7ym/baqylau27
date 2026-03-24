from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from data_access.db.models.gym import Gym

class GymRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Gym]:
        result = await self.db.execute(select(Gym))
        return result.scalars().all()
    
    async def get_by_id(self, gym_id: UUID) -> Gym | None:
        result = await self.db.execute(select(Gym).where(Gym.id == gym_id))
        return result.scalar_one_or_none()
    
    async def create(self, gym: Gym) -> Gym:
        self.db.add(gym)
        await self.db.commit()
        await self.db.refresh(gym)  

        return gym