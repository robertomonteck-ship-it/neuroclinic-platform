from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class TestSessionResponse(Base):
    __tablename__ = "test_session_responses"

    id = Column(Integer, primary_key=True)

    session_id = Column(
        Integer,
        ForeignKey("test_sessions.id")
    )

    question_id = Column(
        Integer,
        ForeignKey("test_template_questions.id")
    )

    selected_option_id = Column(
        Integer,
        ForeignKey("test_template_options.id")
    )

    session = relationship(
        "TestSession",
        back_populates="responses"
    )