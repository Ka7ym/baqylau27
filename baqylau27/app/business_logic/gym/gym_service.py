from fastapi import HTTPException
from data_access.gym.gym_repository import Gym
from data_access.db.models.gym import Gym
from api.gym.gym_schemas import GymRead, GymCreate

from uuid import UUID

class GymService:
    def __init__(self, repo: Gym):
        self.repo = repo

    async def get_gym(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, gym_id: UUID):
        gym = await self.repo.get_by_id(gym_id)

        if not gym:
            raise HTTPException(status_code=404, detail="Gym not found")
        return gym
    
    async def create(self, data: GymCreate):
        gym = Gym(
            name=data.name,
            country=data.country,
            iata_code=data.iata_code
        )

        return await self.repo.create(gym)