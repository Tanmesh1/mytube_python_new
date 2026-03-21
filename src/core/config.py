from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    DEBUG: bool = False

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME:str

    @property
    def DATABASE_URL(self) -> str:
        return(
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    class Config:
        env_file = ".env.dev"


settings = Settings()