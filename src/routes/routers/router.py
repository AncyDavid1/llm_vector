"""
Define Routers (similar to namespaces and blueprint in flask)
"""

from fastapi import APIRouter

llm_prediction_router = APIRouter(
    prefix='/llm'
)
