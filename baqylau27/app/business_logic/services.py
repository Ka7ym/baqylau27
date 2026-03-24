from sqlalchemy.orm import Session
from app.data_access import crud

def get_trainer_service(db: Session, trainer_id: int):
    return crud.get_trainer(db, trainer_id)

def update_trainer_service(db: Session, trainer_id: int, data):
    return crud.update_trainer(db, trainer_id, data)

def delete_trainer_service(db: Session, trainer_id: int):
    return crud.delete_trainer(db, trainer_id)