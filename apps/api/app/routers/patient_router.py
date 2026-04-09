from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

from app.core.database import get_db

from app.schemas.patient import (
    PatientCreate,
    PatientResponse
)

from app.services.patient_service import (
    create_patient,
    get_patients,
    get_patient_by_id
)


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "/",
    response_model=PatientResponse
)
def create_new_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    return create_patient(
        db,
        patient
    )


@router.get(
    "/",
    response_model=List[PatientResponse]
)
def read_patients(
    db: Session = Depends(get_db)
):

    return get_patients(
        db
    )


@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient