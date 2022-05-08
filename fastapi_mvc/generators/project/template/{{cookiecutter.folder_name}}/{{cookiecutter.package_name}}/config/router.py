"""Application configuration - root APIRouter.

Defines all FastAPI application endpoints.

Resources:
    1. https://fastapi.tiangolo.com/tutorial/bigger-applications

"""
from fastapi import APIRouter
from {{cookiecutter.package_name}}.app.controllers import ready

router = APIRouter(prefix="/api")

router.include_router(ready.router, tags=["ready"])
