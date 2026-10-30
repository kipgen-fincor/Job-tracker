from sqlalchemy import create_engine, event #configures how your application is connected to the database
from sqlalchemy.orm import declarative_base , sessionmaker

DATABASE_URL = "sqlite:///job-tracker.db"
engine = create_engine(DATABASE_URL)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    # SQLite ignores foreign keys unless this is switched on for every connection
    dbapi_connection.execute("PRAGMA foreign_keys=ON")


SessionLocal =sessionmaker(
    autocommit = False,
    bind = engine,
    autoflush = False,
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Base =declarative_base()