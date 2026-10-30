from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.documents.User import User


# Temporary: trusts whatever user id the caller sends in the X-User-Id header.
# Replace this with token-based login when authentication is added.
def get_current_user(x_user_id: int = Header(), db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.id == x_user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unknown user")
    return user
