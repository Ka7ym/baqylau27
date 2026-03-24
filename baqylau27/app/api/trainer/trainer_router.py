from fastapi import APIRouter
from . import trainer_router

router = APIRouter(
    prefix="/trainers",
)
router.include_router(
    trainer_router.router,
    tags=["trainers"]
)