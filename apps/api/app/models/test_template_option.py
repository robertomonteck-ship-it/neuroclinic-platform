from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class TestTemplateOption(Base):
    __tablename__ = "test_template_options"

    id = Column(Integer, primary_key=True)

    question_id = Column(
        Integer,
        ForeignKey("test_template_questions.id")
    )

    option_text = Column(Text)

    score_value = Column(Integer)

    question = relationship(
        "TestTemplateQuestion",
        back_populates="options"
    )