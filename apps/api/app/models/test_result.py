from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime

from app.core.database import Base


class TestResult(Base):

    __tablename__ = "test_results"

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

    test_id = Column(
        Integer,
        ForeignKey("psychological_tests.id"),
        nullable=False
    )

    total_score = Column(
        Integer,
        nullable=True
    )

    classification = Column(
        String,
        nullable=True
    )
    # Ex: leve, moderado, severo

    interpretation = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )