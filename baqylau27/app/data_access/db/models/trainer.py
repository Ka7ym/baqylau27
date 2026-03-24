from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from data_access.db.base import Base


class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plant_name = Column(String, nullable=False)
    harvest_year = Column(Integer, nullable=False)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"), nullable=False)

    farm = relationship("train", back_populates="trainers")