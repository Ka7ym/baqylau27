from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.trainer.trainer_schemas import TrainerCreate, TrainerRead
from business_logic.trainer.trainer_service import TrainerService
from data_access.trainer.trainer_repository import TrainerRepository
from data_access.db.session import get_db

router = APIRouter()


def get_trainer_service(db: AsyncSession = Depends(get_db)) -> TrainerService:
    repo = TrainerRepository(db)
    return TrainerService(repo)


@router.get("/all", response_model=list[TrainerRead])
async def get_trainers(
    service: TrainerService = Depends(get_trainer_service),
):
    return await service.get_trainer()


@router.post("/create", response_model=TrainerRead)
async def create_trainer(
    trainer: TrainerCreate,
    service: TrainerService = Depends(get_trainer_service),
):
    try:
        return await service.create(trainer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))