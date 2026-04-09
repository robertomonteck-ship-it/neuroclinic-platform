from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

from app.core.database import get_db

from app.schemas.clinical_note import (
    ClinicalNoteCreate,
    ClinicalNoteResponse
)

from app.services.clinical_note_service import (
    create_clinical_note,
    get_clinical_notes,
    get_clinical_note_by_id
)


router = APIRouter(
    prefix="/clinical-notes",
    tags=["Clinical Notes"]
)


@router.post(
    "/",
    response_model=ClinicalNoteResponse
)
def create_new_note(
    note: ClinicalNoteCreate,
    db: Session = Depends(get_db)
):

    return create_clinical_note(
        db,
        note
    )


@router.get(
    "/",
    response_model=List[ClinicalNoteResponse]
)
def read_notes(
    db: Session = Depends(get_db)
):

    return get_clinical_notes(
        db
    )


@router.get(
    "/{note_id}",
    response_model=ClinicalNoteResponse
)
def read_note(
    note_id: int,
    db: Session = Depends(get_db)
):

    note = get_clinical_note_by_id(
        db,
        note_id
    )

    if not note:

        raise HTTPException(
            status_code=404,
            detail="Clinical note not found"
        )

    return note