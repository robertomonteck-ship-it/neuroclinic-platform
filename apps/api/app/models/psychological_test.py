from sqlalchemy import Column, Integer, String, Text, Boolean

from app.core.database import Base


class PsychologicalTest(Base):

    __tablename__ = "psychological_tests"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    category = Column(
        String,
        nullable=True
    )
    # Ex: memória, atenção, humor

    is_active = Column(
        Boolean,
        default=True
    )