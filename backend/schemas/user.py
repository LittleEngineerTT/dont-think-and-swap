from typing import Self
from uuid import uuid4

from pydantic import BaseModel


class User(BaseModel):
    id: str
    index: int
    session_id: str
    name: str = ""

    @classmethod
    def create_user(cls, index: int, session_id: str, user_id: str = "") -> Self:
        """
        Create a new user without name
        """

        # Check user has a given ID
        if user_id == "":
            user_id = uuid4().hex

        user = User(**{
            "id": user_id,
            "index": index,
            "session_id": session_id
        })

        return user


class RegisterUserBody(BaseModel):
    session_id: str = ""
