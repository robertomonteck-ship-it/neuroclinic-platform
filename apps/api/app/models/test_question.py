from sqlalchemy import Column, Integer, String, ForeignKey, Text

from app.core.database import Base


class TestQuestion(Base):

    __tablename__ = "test_questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    test_id = Column(
        Integer,
        ForeignKey("psychological_tests.id"),
        nullable=False
    )

    question_text = Column(
        Text,
        nullable=False
    )

    question_order = Column(
        Integer,
        nullable=False
    )

    response_type = Column(
        String,
        nullable=False
    )
    # Ex: likert, multiple_choice, numeric