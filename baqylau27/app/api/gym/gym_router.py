from fastapi import APIRouter
from . import gym_router

router = APIRouter(
    prefix="/gyms",
)
router.include_router(
    gym_router.router,
    tags=["gyms"]
)