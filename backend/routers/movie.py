from core.config import get_config
from libs.logger import setup_logger
from schemas.movie import TMDBMovie

from fastapi import APIRouter
from fastapi.responses import JSONResponse


movie = APIRouter(
    prefix="",
    tags=["movie"]
)

# Set up logger
logger = setup_logger("backend.log")


@movie.get("/movie/genres",
          description="Get TMDB movie genres")
async def get_movie_genre():
    genres = await TMDBMovie.get_movie_genre()
    logger.info(f"Movie genre: {genres}")
    genres_name = [genre["name"] for genre in genres]
    return JSONResponse(genres_name)
