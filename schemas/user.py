from models.user import user as userModel

from ipaddress import IPv4Address, IPv6Address
from typing import Self

from pydantic import BaseModel, field_validator, AfterValidator
from re import match
from wakeonlan import send_magic_packet


class User(BaseModel):
    name: str
    last_name: str
    address: str


    @classmethod
    def get_users(cls) -> list[Self]:
        """
        Get all users.
        """
        users = userModel.get_users()
        for user in users:
            user.mac = user.mac.lower()

        return users


    def register(self) -> int:
        """
        Register new user
        :return: status code
        """

        users = self.get_users()

        # Check for duplicate
        for user in users:
            if user.name == self.name:
                return 409

        userModel.add_user(self.dict())
        return 200


    def delete(self) -> None:
        """
        Delete user
        :return: None
        """
        userModel.delete_user(self.dict())
