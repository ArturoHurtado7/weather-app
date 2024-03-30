# FastAPI
from fastapi import APIRouter, status, Query, Depends
from fastapi.responses import JSONResponse

# Services
from src.services import weather_service

from sqlalchemy.orm import Session
from src.database import SessionLocal

router = APIRouter()

def get_db():
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/weather",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Bad request, something went wrong"},
        404: {"description": "City not found"},
        500: {"description": "Internal server error"},
    },
)
async def get_weather(
    city: str = Query(..., min_length=1),
    country: str = Query(..., pattern="^[a-z]{2}$"), 
    db: Session = Depends(get_db)
):
    """
    Get city weather, from cache database or from weather api
    """
    try:
        status_code, content = weather_service(city, country, db)
    except Exception as e:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        content = {"error": str(e)}
    return JSONResponse(status_code=status_code, content=content)

@router.get(
    "/",
    status_code=status.HTTP_200_OK
)
async def health_check():
    """
    Health check
    """
    return {"status": "ok"}