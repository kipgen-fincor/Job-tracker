from sqlalchemy.orm import Session
from src.documents.User import User
from src.models.models import UserCreate
from fastapi import HTTPException


def create_user(db: Session, user_create: UserCreate) -> User:
    existing_user = db.query(User).filter(User.email == user_create.email).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="This email is already registered"
        )

    new_user = User(**user_create.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
