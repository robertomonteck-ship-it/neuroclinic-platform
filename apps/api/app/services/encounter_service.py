from sqlalchemy.orm import Session

from app.models.encounter import Encounter

from app.schemas.encounter import EncounterCreate


def create_encounter(
    db: Session,
    encounter: EncounterCreate
):

    db_encounter = Encounter(
        patient_id=encounter.patient_id,
        professional_id=encounter.professional_id,
        encounter_type=encounter.encounter_type,
        notes=encounter.notes
    )

    db.add(db_encounter)

    db.commit()

    db.refresh(db_encounter)

    return db_encounter


def get_encounters(
    db: Session
):

    return db.query(Encounter).all()


def get_encounter_by_id(
    db: Session,
    encounter_id: int
):

    return db.query(Encounter).filter(
        Encounter.id == encounter_id
    ).first()