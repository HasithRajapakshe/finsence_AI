"""
Centralized settings for this service, loaded from environment variables.
Copy this file into every service (api-gateway, orchestrator, each agent) —
only SERVICE_NAME and PORT differ per service.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    SERVICE_NAME: str = "kyc-agent"
    ENV: str = "development"           # development | staging | production
    PORT: int = 8021
    LOG_LEVEL: str = "INFO"

    # Data layer (Sprint 1 base infra)
    DATABASE_URL: str = "postgresql://finsense:finsense@postgres:5432/finsense"
    REDIS_URL: str = "redis://redis:6379/0"
    QDRANT_URL: str = "http://qdrant:6333"

    # Downstream agent services (filled in as agents come online in later sprints)
    ORCHESTRATOR_URL: str = "http://orchestrator:8010"


settings = Settings()
