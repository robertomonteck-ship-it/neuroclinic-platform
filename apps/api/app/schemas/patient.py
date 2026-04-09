from pydantic import BaseModel
from datetime import date
from typing import Optional


class PatientBase(BaseModel):

    full_name: str

    cpf: str

    birth_date: date

    gender: str

    phone: Optional[str] = None

    email: Optional[str] = None

    address: Optional[str] = None

    city: Optional[str] = None


class PatientCreate(PatientBase):

    pass


class PatientResponse(PatientBase):

    id: int

    is_active: bool

    class Config:

        from_attributes = True