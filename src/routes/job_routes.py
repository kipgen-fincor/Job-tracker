from src.database import *
from src.controllers import job_controller
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.models.models import *
from src.documents.Job import *
from src.documents.User import User
from src.dependencies import get_current_user

router =APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job_create: JobCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return job_controller.create_job(db,current_user.id,job_create)

@router.get("/", response_model=list[JobResponse])
def get_all_jobs(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return job_controller.get_all_jobs(db,current_user.id)

@router.patch("/{job_id}", response_model=JobResponse, status_code=status.HTTP_200_OK)
def update_job(job_update:JobUpdate,job_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    job= job_controller.update_job(db,current_user.id,job_id,job_update)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")
    return job

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = job_controller.get_job_by_id(db, current_user.id, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job
@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = job_controller.delete_job(db, current_user.id, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return {"message": "Job deleted successfully"}
