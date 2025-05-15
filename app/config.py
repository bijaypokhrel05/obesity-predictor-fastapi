from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = "model/obesity_classifier.pkl"

    class Config:
        env_file = ".env"

settings = Settings()
