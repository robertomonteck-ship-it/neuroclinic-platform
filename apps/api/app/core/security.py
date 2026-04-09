import os
import base64
import hashlib
import hmac
from datetime import datetime, timedelta

from jose import jwt

from app.core.settings import settings


def hash_password(password: str) -> str:
    salt = os.urandom(16)

    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000,
    )

    return base64.b64encode(salt + key).decode("utf-8")


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    decoded = base64.b64decode(
        hashed_password.encode("utf-8")
    )

    salt = decoded[:16]
    stored_key = decoded[16:]

    new_key = hashlib.pbkdf2_hmac(
        "sha256",
        plain_password.encode("utf-8"),
        salt,
        100000,
    )

    return hmac.compare_digest(
        stored_key,
        new_key
    )


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt