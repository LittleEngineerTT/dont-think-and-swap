from typing import Self
from uuid import uuid4

from pydantic import BaseModel


class User(BaseModel):
    id: str
    index: int
    session_id: str
    name: str = ""

    @classmethod
    def create_user(cls, index: int, session_id: str) -> Self:
        """
        Create a new user without name
        """
        user = User(**{
            "id": uuid4().hex,
            "index": index,
            "session_id": session_id
        })

        return user
