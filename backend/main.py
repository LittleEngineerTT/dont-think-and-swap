from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

# Create FastAPI instance
app = FastAPI(lifespan=lifespan)


# Set CORS settings
origins = [
    "http://localhost:8080"
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
    uvicorn.run("main:app", host='0.0.0.0', port=8000, workers=1)
