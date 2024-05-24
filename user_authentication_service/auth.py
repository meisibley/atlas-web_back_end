#!/usr/bin/env python3
""" authentication methods """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password, hashed
    with bcrypt.hashpw.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """ return a string representation of a new UUID """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ If a user already exist with the passed email, raise a ValueError
        with the message User <user's email> already exists. If not, hash the
        password with _hash_password, save the user to the database using
        self._db and return the User object."""
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            save_user = self._db.add_user(email, hashed_pwd)
            return save_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Try locating the user by email. If it exists, check the password
        with bcrypt.checkpw. If it matches return True. In any other case,
        return False.
        """
        try:
            found_user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(bytes(password, "ascii"),
                                  found_user.hashed_password)
        except NoResultFound:
            return False
