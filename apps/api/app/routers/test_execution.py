from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import SessionLocal

from app.models.test_session import TestSession
from app.models.test_session_response import TestSessionResponse
from app.models.test_template_option import TestTemplateOption
from app.models.scoring_rules import TestScoringRule

router = APIRouter(
    prefix="/tests",
    tags=["Test Execution"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ----------------------------------------
# Iniciar teste
# ----------------------------------------

@router.post("/start")
def start_test(
    patient_id: int,
    template_id: int,
    db: Session = Depends(get_db)
):

    session = TestSession(
        patient_id=patient_id,
        template_id=template_id
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


# ----------------------------------------
# Responder pergunta
# ----------------------------------------

@router.post("/{session_id}/answer")
def answer_question(
    session_id: int,
    question_id: int,
    selected_option_id: int,
    db: Session = Depends(get_db)
):

    response = TestSessionResponse(
        session_id=session_id,
        question_id=question_id,
        selected_option_id=selected_option_id
    )

    db.add(response)
    db.commit()

    return {"message": "Resposta salva"}


# ----------------------------------------
# Finalizar teste
# ----------------------------------------

@router.post("/{session_id}/finish")
def finish_test(
    session_id: int,
    db: Session = Depends(get_db)
):

    responses = db.query(
        TestSessionResponse
    ).filter(
        TestSessionResponse.session_id == session_id
    ).all()

    total_score = 0

    for r in responses:

        option = db.query(
            TestTemplateOption
        ).filter(
            TestTemplateOption.id == r.selected_option_id
        ).first()

        total_score += option.score_value

    session = db.query(TestSession).get(session_id)

    session.finished_at = datetime.utcnow()
    session.status = "finished"

    rules = db.query(TestScoringRule).filter(
        TestScoringRule.template_id == session.template_id
    ).all()

    interpretation = "Unknown"

    for rule in rules:

        if rule.min_score <= total_score <= rule.max_score:

            interpretation = rule.interpretation

    db.commit()

    return {
        "total_score": total_score,
        "interpretation": interpretation
    }