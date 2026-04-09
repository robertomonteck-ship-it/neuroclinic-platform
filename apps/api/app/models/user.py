from sqlalchemy import Column, Integer, String, Boolean

# IMPORTANTE — usar Base do database
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String, nullable=False)

    cpf = Column(String, unique=True, nullable=False)

    profession = Column(String, nullable=False)
    # psychologist | psychiatrist | admin

    crp_number = Column(String, nullable=True)

    crm_number = Column(String, nullable=True)

    rqe_number = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)