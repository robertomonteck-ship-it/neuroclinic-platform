from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

from app.core.database import get_db

from app.schemas.encounter import (
    EncounterCreate,
    EncounterResponse
)

from app.services.encounter_service import (
    create_encounter,
    get_encounters,
    get_encounter_by_id
)


router = APIRouter(
    prefix="/encounters",
    tags=["Encounters"]
)


@router.post(
    "/",
    response_model=EncounterResponse
)
def create_new_encounter(
    encounter: EncounterCreate,
    db: Session = Depends(get_db)
):

    return create_encounter(
        db,
        encounter
    )


@router.get(
    "/",
    response_model=List[EncounterResponse]
)
def read_encounters(
    db: Session = Depends(get_db)
):

    return get_encounters(
        db
    )


@router.get(
    "/{encounter_id}",
    response_model=EncounterResponse
)
def read_encounter(
    encounter_id: int,
    db: Session = Depends(get_db)
):

    encounter = get_encounter_by_id(
        db,
        encounter_id
    )

    if not encounter:

        raise HTTPException(
            status_code=404,
            detail="Encounter not found"
        )

    return encounter