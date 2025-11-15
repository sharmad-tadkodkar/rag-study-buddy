from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/postgres"
    OPENAI_API_KEY: str = ""
    CHROMA_PERSIST: str = "/data/chroma"
    class Config:
        env_file = ".env"

settings = Settings()
