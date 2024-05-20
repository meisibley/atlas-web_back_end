#!/usr/bin/env python3
""" Create the class Auth """
from flask import request
from typing import List, TypeVar


class Auth:
    """ class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method def require_auth(self, path: str, excluded_paths:
        List[str]) -> bool: that returns False - path and excluded_paths will
        be used later, now, you don’t need to take care of them """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ public method def authorization_header(self, request=None) -> str:
        that returns None - request will be the Flask request object"""
        if request is None:
            return None
        if not request.header.get('Authorization'):
            return None
        return request.header.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method def current_user(self, request=None) ->
        TypeVar('User'): that returns None - request will be the Flask
        request object"""
        return None
