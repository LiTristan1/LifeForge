from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

human_health_router = APIRouter()

@human_health_router.get("/get/{stat}")
def getStat(stat: str):
    return JSONResponse(status_code=status.HTTP_200_OK,content=stat)
