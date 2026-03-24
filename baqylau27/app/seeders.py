import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.trainer import Trainer
from data_access.db.models.gym import Gym
from data_access.db.session import AsyncSessionLocal


async def seed_trainers(db: AsyncSession):
    trainers_data = [
        {"name": "Sunrise Trainer", "region": "Almaty",   "area_hectares": 150.5},
        {"name": "Green Valley Trainer", "region": "Kostanay", "area_hectares": 320.0},
        {"name": "Steppe Gold Trainer",  "region": "Akmola",   "area_hectares": 500.0},
    ]
    for t in trainers_data:
        result = await db.execute(select(Trainer).where(Trainer.name == t["name"]))
        exists = result.scalar_one_or_none()
        if not exists:
            trainer = Trainer(
                name=t["name"],
                region=t["region"],
                area_hectares=t["area_hectares"]
            )
            db.add(trainer)
    await db.commit()


async def seed_gyms(db: AsyncSession):
    """Gym кестесін толтыру, Trainer Foreign Key бар екенін тексеру"""
    result = await db.execute(select(Trainer).where(Trainer.name == "Sunrise Trainer"))
    sunrise_trainer = result.scalar_one_or_none()
    if not sunrise_trainer:
        sunrise_trainer = Trainer(name="Sunrise Trainer", region="Almaty", area_hectares=150.5)
        db.add(sunrise_trainer)
        await db.commit()
        await db.refresh(sunrise_trainer)

    result = await db.execute(select(Trainer).where(Trainer.name == "Green Valley Trainer"))
    green_valley = result.scalar_one_or_none()
    if not green_valley:
        green_valley = Trainer(name="Green Valley Trainer", region="Kostanay", area_hectares=320.0)
        db.add(green_valley)
        await db.commit()
        await db.refresh(green_valley)

    result = await db.execute(select(Trainer).where(Trainer.name == "Steppe Gold Trainer"))
    steppe_gold = result.scalar_one_or_none()
    if not steppe_gold:
        steppe_gold = Trainer(name="Steppe Gold Trainer", region="Akmola", area_hectares=500.0)
        db.add(steppe_gold)
        await db.commit()
        await db.refresh(steppe_gold)

    result = await db.execute(select(Trainer))
    trainers_in_db = result.scalars().all()
    print("Trainers in DB:", [(t.id, t.name) for t in trainers_in_db])

    gyms_data = [
        {"plant_name": "Wheat",     "harvest_year": 2023, "trainer": sunrise_trainer},
        {"plant_name": "Sunflower", "harvest_year": 2023, "trainer": sunrise_trainer},
        {"plant_name": "Barley",    "harvest_year": 2024, "trainer": green_valley},
        {"plant_name": "Corn",      "harvest_year": 2024, "trainer": green_valley},
        {"plant_name": "Rapeseed",  "harvest_year": 2023, "trainer": steppe_gold},
        {"plant_name": "Wheat",     "harvest_year": 2024, "trainer": steppe_gold},
    ]

    for g in gyms_data:
        result = await db.execute(
            select(Gym).where(
                (Gym.plant_name == g["plant_name"]) &
                (Gym.farm_id == g["trainer"].id)
            )
        )
        exists = result.scalar_one_or_none()
        if not exists:
            gym = Gym(
                plant_name=g["plant_name"],
                harvest_year=g["harvest_year"],
                farm_id=g["trainer"].id
            )
            db.add(gym)
    await db.commit()


async def run_seeders(db: AsyncSession):
    await seed_trainers(db)
    await seed_gyms(db)


async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)


if __name__ == "__main__":
    asyncio.run(main())