from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.gym.gym_schemas import GymCreate, GymRead
from business_logic.gym.gym_service import GymService
from data_access.gym.gym_repository import GymRepository
from data_access.db.session import get_db

router = APIRouter()


def get_gym_service(db: AsyncSession = Depends(get_db)) -> GymService:
    repo = GymRepository(db)
    return GymService(repo)


@router.get("/all", response_model=list[GymRead])
async def get_gyms(
    service: GymService = Depends(get_gym_service),
):
    return await service.get_gym()


@router.post("/create", response_model=GymRead)
async def create_gym(
    gym: GymCreate,
    service: GymService = Depends(get_gym_service),
):
    try:
        return await service.create(gym)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))