from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Encounter(Base):

    __tablename__ = "encounters"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    professional_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    encounter_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    encounter_type = Column(
        String,
        nullable=False
    )
    # Ex: avaliação, retorno, triagem

    notes = Column(
        Text,
        nullable=True
    )

    # Relacionamentos
    patient = relationship("Patient")

    professional = relationship("User")