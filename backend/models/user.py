"""
This file is useful to abstract database implementation
"""

from core.database import get_db, Base

from typing import Self

from sqlalchemy import Column, String, func


class User(Base):
    """
    Class to interact with a user inside the database.
    """

    __tablename__ = 'users'
    name = Column(String, nullable=False)
    last_name = Column(String, primary_key=True, nullable=False, unique=True)
    address = Column(String, nullable=False, unique=True)


    @classmethod
    def get_users(cls) -> list[Self]:
        """
        Get all users
        """
        users = None
        db = get_db()
        try:
            users = db.query(cls).all()
        finally:
            db.close()
            return users


    @classmethod
    def add_user(cls, user: Self) -> None:
        """
        Add user to the database.
        """
        db = get_db()
        try:
            user_instance = cls(**user)
            db.add(user_instance)

            # Save changes
            db.commit()
        finally:
            db.close()


    @classmethod
    def delete_user(cls, user: Self) -> None:
        """
        Delete user from the database.
        """
        db = get_db()
        try:
            user_instance = db.query(cls).filter(func.lower(cls.mac) == user["mac"].lower()).first()
            db.delete(user_instance)

            # Save changes
            db.commit()
        finally:
            db.close()
