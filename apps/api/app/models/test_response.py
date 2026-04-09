from sqlalchemy import Column, Integer, String, ForeignKey, Text

from app.core.database import Base


class TestResponse(Base):

    __tablename__ = "test_responses"

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

    question_id = Column(
        Integer,
        ForeignKey("test_questions.id"),
        nullable=False
    )

    response_value = Column(
        String,
        nullable=False
    )
    # Ex: "0", "1", "2", "3"

    response_text = Column(
        Text,
        nullable=True
    )