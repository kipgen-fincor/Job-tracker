from sqlalchemy.orm import Session
from src.documents.Job import Job
from src.models.models import JobUpdate,JobCreate
from fastapi import APIRouter,Depends,HTTPException,status


def create_job(db: Session, user_id: int, job_create: JobCreate) -> Job:
    existing_job = db.query(Job).filter(
        Job.user_id == user_id,
        Job.company_name == job_create.company_name,
        Job.job_title == job_create.job_title
    ).first()

    if existing_job:
        raise HTTPException(
            status_code=409,
            detail="You have already added this job"
        )

    new_job = Job(**job_create.model_dump(), user_id=user_id)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def get_all_jobs(db:Session, user_id: int):
    return db.query(Job).filter(Job.user_id == user_id).all()

def get_job_by_id(db: Session, user_id: int, job_id: int):
    return db.query(Job).filter(Job.id == job_id, Job.user_id == user_id).first()

def update_job(db: Session, user_id: int, job_id: int, job_update: JobUpdate):
    job = get_job_by_id(db, user_id, job_id)
    if job is None:
        return None
    update_data =job_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="At least one field must be provided"
        )

    for key, value in update_data.items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)

    return job

def delete_job(db: Session, user_id: int, job_id: int):
    job = get_job_by_id(db, user_id, job_id)

    if job is None:
        return None

    db.delete(job)
    db.commit()

    return job
