"""
FastAPI boilerplate — this is the Sprint 1 "shared service template" referenced
in the Development Plan (Section 5, Sprint 1). Every agent service and the
API gateway starts from this exact file, with SERVICE_NAME/PORT changed via
.env and business routes added under app/routers/.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import time

from app.config import settings
from app.logging_config import configure_logging

logger = configure_logging(settings.SERVICE_NAME, settings.LOG_LEVEL)

app = FastAPI(
    title=f"FinSense AI — {settings.SERVICE_NAME}",
    version="0.1.0",
    docs_url="/docs" if settings.ENV != "production" else None,
)

# CORS: tightened per-service before Sprint 8 hardening; open for local dev only.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8081"] if settings.ENV == "development" else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration_ms = round((time.time() - start) * 1000, 2)
    logger.info(
        "request_handled",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )
    return response


@app.get("/health")
async def health():
    """Liveness/readiness probe — required before this service is added to
    docker-compose healthchecks or a k8s deployment."""
    return JSONResponse({"status": "ok", "service": settings.SERVICE_NAME})


@app.get("/")
async def root():
    return {"service": settings.SERVICE_NAME, "env": settings.ENV}

# Business routers get included here in later sprints, e.g.:
# from app.routers import applications
# app.include_router(applications.router, prefix="/v1/applications", tags=["applications"])
