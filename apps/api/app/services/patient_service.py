from sqlalchemy.orm import Session

from app.models.patient import Patient

from app.schemas.patient import PatientCreate


def create_patient(
    db: Session,
    patient: PatientCreate
):

    db_patient = Patient(
        full_name=patient.full_name,
        cpf=patient.cpf,
        birth_date=patient.birth_date,
        gender=patient.gender,
        phone=patient.phone,
        email=patient.email,
        address=patient.address,
        city=patient.city
    )

    db.add(db_patient)

    db.commit()

    db.refresh(db_patient)

    return db_patient


def get_patients(
    db: Session
):

    return db.query(Patient).all()


def get_patient_by_id(
    db: Session,
    patient_id: int
):

    return db.query(Patient).filter(
        Patient.id == patient_id
    ).first()