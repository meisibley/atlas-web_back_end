#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add new users with their email and hashed pwd into DB users table
        return a User object """
        add_usr = User(email=email, hashed_password=hashed_password)
        self._session.add(add_usr)
        self._session.commit()
        return add_usr

    def find_user_by(self, **kwargs) -> User:
        """ takes in arbitrary keyword arguments and returns the first row
        found in the users table as filtered by the method’s input arguments.
        No validation of input arguments required at this point."""
        for key in kwargs.keys():
            if key not in User.__table__.columns:
                raise InvalidRequestError()
        got_key = self._session.query(User).filter_by(**kwargs).one_or_none()
        if got_key is None:
            raise NoResultFound()
        return got_key
