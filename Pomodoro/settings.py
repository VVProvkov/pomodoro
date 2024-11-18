from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = '0.0.0.0'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '1234'
    DB_DRIVER: str = 'postgresql+psycopg'
    DB_NAME: str = 'pomodoro'
    CACHE_HOST: str = '0.0.0.0'
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0
    
    @property
    def db_url(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@P{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'