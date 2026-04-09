from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EncounterBase(BaseModel):

    patient_id: int

    professional_id: int

    encounter_type: str

    notes: Optional[str] = None


class EncounterCreate(EncounterBase):

    pass


class EncounterResponse(EncounterBase):

    id: int

    encounter_date: datetime

    class Config:

        from_attributes = True