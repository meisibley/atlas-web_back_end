#!/usr/bin/env python3
""" Create the class Auth """
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method def require_auth(self, path: str, excluded_paths:
        List[str]) -> bool: in Auth that returns True if the path is not in
        the list of strings excluded_paths:
        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        You can assume excluded_paths contains string path always ending
        by a /
        This method must be slash tolerant: path=/api/v1/status and
        path=/api/v1/status/ must be returned False if excluded_paths contains
        /api/v1/status/
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) is None:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ public method def authorization_header(self, request=None) -> str:
        that returns None - request will be the Flask request object - task3
        If request is None, returns None
        If request doesn’t contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization"""
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method def current_user(self, request=None) ->
        TypeVar('User'): that returns None - request will be the Flask
        request object"""
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request:
        Return None if request is None
        Return the value of the cookie named _my_session_id from request
        - the name of the cookie must be defined by the environment
        variable SESSION_NAME
        You must use .get() built-in for accessing the cookie in the request
        cookies dictionary
        You must use the environment variable SESSION_NAME to define the name
        of the cookie used for the Session ID """
        if request is None:
            return None
        SESSION_NAME = getenv("SESSION_NAME")
        _my_session_id = request.cookies.get(SESSION_NAME)
        return _my_session_id
