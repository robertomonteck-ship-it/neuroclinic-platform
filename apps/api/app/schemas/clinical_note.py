from pydantic import BaseModel
from datetime import datetime


class ClinicalNoteBase(BaseModel):

    encounter_id: int

    professional_id: int

    note_text: str


class ClinicalNoteCreate(ClinicalNoteBase):

    pass


class ClinicalNoteResponse(ClinicalNoteBase):

    id: int

    created_at: datetime

    class Config:

        from_attributes = True