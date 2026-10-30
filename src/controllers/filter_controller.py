from sqlalchemy.orm import Session
from src.documents.Job import Job
from sqlalchemy import or_

def search_jobs(
            db: Session,
            user_id: int,
            search: str | None = None,
            status: str | None = None,
            location: str | None = None,
            sort_by: str = "applied_date",
            order: str = "desc",
    ):
        query = db.query(Job).filter(Job.user_id == user_id)

        if search:
            search_term = f"%{search}%"
            query = query.filter(
                or_(
                    Job.company_name.ilike(search_term),
                    Job.job_title.ilike(search_term),
                )
            )

        if status:
            query = query.filter(Job.status == status)

        if location:
            query = query.filter(Job.location.ilike(f"%{location}%"))

        sort_columns = {
            "company_name": Job.company_name,
            "applied_date": Job.applied_date,
        }

        if sort_by not in sort_columns:
            raise ValueError("Invalid sort_by field")

        if order not in ("asc", "desc"):
            raise ValueError("Invalid sort order")

        sort_column = sort_columns[sort_by]

        if order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

        return query.all()
