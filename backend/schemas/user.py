from models.user import user as userModel

from pydantic import BaseModel


class User(BaseModel):
    id: str
    number: int
    name: str = ""
