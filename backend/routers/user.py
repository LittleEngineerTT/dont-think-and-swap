from libs.logger import setup_logger
from schemas.session import session_manager
from schemas.user import User, RegisterUserBody, GetInvitationBody

from uuid import uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

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

    # Create user
    if body.user_id != "":
        # Invited user
        new_user = User.create_user(index, session_id, body.user_id)
    else:
        new_user = User.create_user(index, session_id)

    if not session_manager.add_user(session_id, new_user):
        raise HTTPException(status_code=500, detail="Could not add user to the session")

    logger.info(f"User ID: {new_user.id}")
    return new_user



@user.post("/user/invitation", response_model=str, description="Create an invitation link\n"
                                                                  "- **session_id**: The ID of the user session")
def get_invitation_link(body: GetInvitationBody):
    session_id = body.session_id
    host = body.host
    port = body.port
    user_id = uuid4().hex

    url_link = f"http://{host}:{port}/invitation/{session_id}/{user_id}"

    return JSONResponse({"url": url_link})
