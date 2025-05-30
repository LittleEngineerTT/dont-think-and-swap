from core.config import get_config
from typing import List, Optional

from pydantic import BaseModel

import requests

config = get_config()

class Movie(BaseModel):
    adult: bool = True
    backdrop_path: Optional[str] = None
    genre_ids: List[int] = None
    id: int = 0
    original_language: str = ""
    original_title: str = ""
    overview: str = ""
    popularity: float = 0.0
    poster_path: Optional[str] = None
    release_date: str = ""
    title: str = ""
    video: bool = True
    vote_average: float = 0.0
    vote_count: int = 0


class TMDBMovie(BaseModel):
    page: int = 0
    results: List[Movie] = None
    total_pages: int = 0
    total_results: int = 0

    @classmethod
    async def get_genres(cls) -> Optional[Movie]:
        url = f'{config["tmdb_api_url"]}genre/movie/list?language=en'

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config['api_key']}"
        }

        response = requests.get(url, headers=headers)
        return response.json()["genres"]
