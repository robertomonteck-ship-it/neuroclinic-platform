from sqlalchemy import Column, Integer, ForeignKey, String

from app.core.database import Base


class TestScoringRule(Base):
    __tablename__ = "test_scoring_rules"

    id = Column(Integer, primary_key=True)

    template_id = Column(
        Integer,
        ForeignKey("test_templates.id")
    )

    min_score = Column(Integer)

    max_score = Column(Integer)

    interpretation = Column(String)