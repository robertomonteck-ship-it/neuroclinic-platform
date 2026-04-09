from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class TestSession(Base):
    __tablename__ = "test_sessions"

    id = Column(Integer, primary_key=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    template_id = Column(
        Integer,
        ForeignKey("test_templates.id")
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    finished_at = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String,
        default="in_progress"
    )

    responses = relationship(
        "TestSessionResponse",
        back_populates="session",
        cascade="all, delete"
    )