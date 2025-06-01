from contextlib import asynccontextmanager
from routers.movie import movie as movie_router
from routers.user import user as user_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

# Create FastAPI instance
app = FastAPI(lifespan=lifespan)

app.include_router(movie_router)
app.include_router(user_router)

# Set CORS settings
origins = [
    #"http://localhost:8080",
    "localhost" # Dev mode only
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=["OPTIONS", "GET", "POST"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to WOL manager"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=3000, workers=1)
