import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "LLM Benchmark Simulation"
    PROJECT_DESCRIPTION: str = "Benchmarking various LLMs against quality metrics."
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
