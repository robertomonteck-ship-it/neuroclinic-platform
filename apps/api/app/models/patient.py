from sqlalchemy import Column, Integer, String, Date, Boolean

from app.core.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    cpf = Column(
        String,
        unique=True,
        nullable=False
    )

    birth_date = Column(
        Date,
        nullable=False
    )

    gender = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=True
    )

    email = Column(
        String,
        nullable=True
    )

    address = Column(
        String,
        nullable=True
    )

    city = Column(
        String,
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )