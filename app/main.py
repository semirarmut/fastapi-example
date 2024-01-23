from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.app_logger import app_logger
from app.utils.middleware import log_middleware
from app.routers import hello_world


def init_app():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app_logger.info("--- Start up App ---")
        yield
        app_logger.info("--- Shut down App ---")

    apps = FastAPI(title="Fast API", lifespan=lifespan)
    apps.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

    @apps.get('/')
    def root():
        return "welcome!"

    apps.include_router(hello_world.router)

    return apps


app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
