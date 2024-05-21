#!/usr/bin/env python3
""" class BasicAuth inherits from Auth """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth inherits from Auth 
    method extract_base64_authorization_header in this class returns Base64
    part of the Authorization header for a Basic Authentication:
    Return None if authorization_header is None
    Return None if authorization_header is not a string
    Return None if authorization_header doesn’t start by Basic
    (with a space at the end)
    Otherwise, return the value after Basic (after the space)
    You can assume authorization_header contains only one Basic """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
