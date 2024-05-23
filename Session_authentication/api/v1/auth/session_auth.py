#!/usr/bin/env python3
""" class SessionAuth that inherits from Auth """
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ For the moment this class will be empty. It’s the first step for
    creating a new authentication mechanism:
    validate if everything inherits correctly without any overloading
    validate the “switch” by using environment variables"""
    pass