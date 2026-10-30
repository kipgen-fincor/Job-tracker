from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.controllers import user_controller
from src.database import get_db
from src.dependencies import get_current_user
from src.documents.User import User
from src.models.models import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user_create)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
