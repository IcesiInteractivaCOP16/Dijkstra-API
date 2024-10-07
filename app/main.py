from fastapi import FastAPI

from app.api.dijkstra import dijkstra

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs")

app.include_router(dijkstra, prefix='/api/v1/dijkstra', tags=['dijkstra'])