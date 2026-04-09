from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class TestTemplate(Base):
    __tablename__ = "test_templates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    code = Column(String, unique=True, nullable=False)

    description = Column(Text)

    total_questions = Column(Integer)

    scoring_type = Column(String)

    is_active = Column(Boolean, default=True)

    questions = relationship(
        "TestTemplateQuestion",
        back_populates="template",
        cascade="all, delete"
    )