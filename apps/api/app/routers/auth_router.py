from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from jose import jwt, JWTError

from app.core.database import get_db
from app.core.security import create_access_token
from app.core.settings import settings

from app.services.auth_service import (
    authenticate_user,
    get_user_by_email
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        email,
        password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def read_users_me(
    token: str,
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email: str = payload.get("sub")

        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = get_user_by_email(
        db,
        email
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "profession": user.profession
    }