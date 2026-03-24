from fastapi import APIRouter
from api.farm.farm_api import router as farm_router
from api.crop.crop_api import router as crop_router

api_router = APIRouter()

api_router.include_router(
    farm_router,
    prefix="/api"
)

api_router.include_router(
    crop_router,
    prefix="/api"
)