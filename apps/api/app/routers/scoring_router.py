from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.scoring_service import (
    calculate_test_score
)


router = APIRouter(
    prefix="/scoring",
    tags=["Scoring"]
)


@router.post("/calculate")
def calculate_score(
    encounter_id: int,
    test_id: int,
    db: Session = Depends(get_db)
):

    return calculate_test_score(
        db,
        encounter_id,
        test_id
    )