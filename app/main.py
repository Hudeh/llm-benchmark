from fastapi import FastAPI
from api.v1.endpoints import rankings
from api.v1.endpoints import simulations
from core.config import settings
from db.base import Base
from db.session import engine

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

# Include API routers
app.include_router(rankings.router, prefix="/api/v1/rankings", tags=["rankings"])
app.include_router(simulations.router, prefix="/api/v1/simulations")