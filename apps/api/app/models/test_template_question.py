from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class TestTemplateQuestion(Base):
    __tablename__ = "test_template_questions"

    id = Column(Integer, primary_key=True)

    template_id = Column(
        Integer,
        ForeignKey("test_templates.id")
    )

    question_number = Column(Integer)

    question_text = Column(Text)

    template = relationship(
        "TestTemplate",
        back_populates="questions"
    )

    options = relationship(
        "TestTemplateOption",
        back_populates="question",
        cascade="all, delete"
    )