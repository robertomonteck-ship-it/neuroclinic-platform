from sqlalchemy.orm import Session

from app.models.clinical_note import ClinicalNote

from app.schemas.clinical_note import ClinicalNoteCreate


def create_clinical_note(
    db: Session,
    note: ClinicalNoteCreate
):

    db_note = ClinicalNote(
        encounter_id=note.encounter_id,
        professional_id=note.professional_id,
        note_text=note.note_text
    )

    db.add(db_note)

    db.commit()

    db.refresh(db_note)

    return db_note


def get_clinical_notes(
    db: Session
):

    return db.query(ClinicalNote).all()


def get_clinical_note_by_id(
    db: Session,
    note_id: int
):

    return db.query(ClinicalNote).filter(
        ClinicalNote.id == note_id
    ).first()