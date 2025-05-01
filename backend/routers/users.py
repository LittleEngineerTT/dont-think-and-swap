from core.config import get_config
from libs.logger import setup_logger
from schemas.user import User

from fastapi import APIRouter, HTTPException

users = APIRouter(
    prefix="",
    tags=["users"]
)

# Get config
config = get_config()

# Set up logger
logger = setup_logger("config.log")


@users.get("/users")
def retrieve_users():
    users = user.get_users()
    return {"users": users}


@users.post("/register")
def register_user(user: user):
    logger.info("Registering user %s", user.name)
    status_code = user.register()

    if status_code != 200:
        raise HTTPException(status_code=status_code)

    return


@users.post("/delete")
def delete_user(user: user):
    logger.info("Deleting user %s", user.name)
    user.delete()
    return
