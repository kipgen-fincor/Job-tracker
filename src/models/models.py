
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.utils.enums import jobStatus


class JobCreate(BaseModel):
    company_name: str = Field(min_length=1, max_length=50)
    status: jobStatus =jobStatus.APPLIED
    job_title: str = Field(min_length=1, max_length=50)
    job_url: str | None = Field(default=None, min_length=1, max_length=50)
    location: str | None = Field(default=None, min_length=1, max_length=50)
    applied_date: datetime | None = None


class JobUpdate(BaseModel):
    company_name: str | None = Field(default=None, min_length=1, max_length=50)
    job_title: str | None = Field(default=None, min_length=1, max_length=50)
    job_url: str | None = Field(default=None, min_length=1, max_length=50)
    status: jobStatus |None =None
    location: str | None = Field(default=None, min_length=1, max_length=50)
    applied_date: datetime | None = None


class JobResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    job_url: str | None = None
    status: jobStatus
    location: str | None = None
    applied_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: str = Field(min_length=3, max_length=255)


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
