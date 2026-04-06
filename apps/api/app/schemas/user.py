from pydantic import BaseModel, EmailStr
from typing import Optional


# Base comum

class UserBase(BaseModel):

    full_name: str

    email: EmailStr

    cpf: str

    profession: str
    # psychologist | psychiatrist | admin

    crp_number: Optional[str] = None

    crm_number: Optional[str] = None

    rqe_number: Optional[str] = None


# Criação de usuário

class UserCreate(UserBase):

    password: str


# Retorno do usuário

class UserOut(UserBase):

    id: int

    is_active: bool

    class Config:

        from_attributes = True