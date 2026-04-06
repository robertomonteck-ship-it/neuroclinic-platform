from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def get_user_by_email(
    db: Session,
    email: str
):

    return db.query(User).filter(
        User.email == email
    ).first()


def create_user(
    db: Session,
    user_data: UserCreate
):

    hashed_password = hash_password(
        user_data.password
    )

    db_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        cpf=user_data.cpf,
        profession=user_data.profession,
        crp_number=user_data.crp_number,
        crm_number=user_data.crm_number,
        rqe_number=user_data.rqe_number,
        password_hash=hashed_password,
        is_active=True
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user