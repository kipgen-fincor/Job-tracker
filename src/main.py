from fastapi import FastAPI

from src.database import engine
from src.routes.job_routes import router
from src.routes import job_routes,search_routes,user_routes
from src.documents.Job import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routes.router)
app.include_router(search_routes.router)  # must come before the jobs router
app.include_router(router)
@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", reload=True)
