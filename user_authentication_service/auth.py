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

    def create_session(self, email: str) -> str:
        """ A method takes an email string argument and returns the session
        ID as a string. The method should find the user corresponding to the
        email, generate a new UUID and store it in the database as the user’s
        session_id, then return the session ID. """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        user.session_id = session_id
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ If the session ID is None or no user is found, return None.
        Otherwise return the corresponding user. """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ The method updates the corresponding user’s session ID to None"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Find the user corresponding to the email. If the user does not
        exist, raise a ValueError exception. If it exists, generate a UUID
        and update the user’s reset_token database field. Return the token"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
        except Exception:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """ Use the reset_token to find the corresponding user. If it does not
        exist, raise a ValueError exception. Otherwise, hash the password and
        update the user’s hashed_password field with the new hashed password
        and the reset_token field to None. """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                user.hashed_password = _hash_password(password)
                self._db.update_user(user.id, reset_token=None)
        except Exception:
            raise ValueError()
