from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from src.database import Base


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    job_url = Column(String, nullable=True)
    status = Column(String, nullable=False)
    location = Column(String, nullable=True)
    applied_date = Column(DateTime, nullable=True)