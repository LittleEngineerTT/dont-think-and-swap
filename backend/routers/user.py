from libs.logger import setup_logger
from schemas.session import session_manager
from schemas.user import User, RegisterUserBody

from fastapi import APIRouter, HTTPException

user = APIRouter(
    prefix="",
    tags=["user"]
)

# Set up logger
logger = setup_logger("config.log")


@user.post("/user/registration", response_model=User, description="Create a new user\n"
                                                                  "- **session_id**: The ID of the user session")
def register_user(body: RegisterUserBody):
    session_id = body.session_id
    if session_id == "":
        # Main user
        session_id = session_manager.create_session()
        index = 0
        if not session_id:
            raise HTTPException(status_code=500, detail="Could not create new session")
    else:
        index = session_manager.users[session_id]["total_users"]
    new_user = User.create_user(index, session_id)

    if not session_manager.add_user(session_id, new_user):
        raise HTTPException(status_code=500, detail="Could not add user to the session")

    logger.info(f"User ID: {new_user.id}")
    return new_user
