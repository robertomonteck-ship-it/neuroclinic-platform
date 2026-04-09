from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class ClinicalNote(Base):

    __tablename__ = "clinical_notes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    encounter_id = Column(
        Integer,
        ForeignKey("encounters.id"),
        nullable=False
    )

    professional_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    note_text = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relacionamentos
    encounter = relationship("Encounter")

    professional = relationship("User")