from typing import Literal

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.controllers.filter_controller import search_jobs
from src.database import get_db
from src.dependencies import get_current_user
from src.documents.User import User
from src.models.models import JobResponse

router = APIRouter(prefix="/jobs", tags=["Search"])
@router.get("/search", response_model=list[JobResponse])
def search_job( search: str | None = None,
    status: str | None = None,
    location: str | None = None,
    sort_by: Literal["company_name", "applied_date"] = "applied_date",
    order: Literal["asc", "desc"] = "desc",
    db: Session = Depends (get_db),
    current_user: User = Depends(get_current_user),):

    return search_jobs(
        db=db,
        user_id=current_user.id,
        search=search,
        status=status,
        location=location,
        sort_by=sort_by,
        order=order,
    )
