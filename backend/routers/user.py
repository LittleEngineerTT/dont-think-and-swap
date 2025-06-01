from libs.logger import setup_logger

from uuid import uuid4

from fastapi import APIRouter

user = APIRouter(
    prefix="",
    tags=["user"]
)

# Set up logger
logger = setup_logger("config.log")


@user.get("/user/id")
def get_user_id():
    random_id = uuid4().hex
    logger.info(f"User ID: {random_id}")
    return random_id
