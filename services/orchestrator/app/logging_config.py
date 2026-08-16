"""
Structured JSON logging — every service logs the same way so Langfuse/Grafana
ingestion in later sprints doesn't need per-service parsing rules.
"""
import logging
from pythonjsonlogger import jsonlogger


def configure_logging(service_name: str, level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(service_name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.handlers = [handler]
    return logger
