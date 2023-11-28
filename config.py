from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # api_key: str = "saket"
    DB_HOST: str

    model_config = SettingsConfigDict(env_file=".env") 

settings = Settings()