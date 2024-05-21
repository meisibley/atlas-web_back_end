#!/usr/bin/env python3
""" class BasicAuth inherits from Auth """
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ BasicAuth inherits from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ method extract_base64_authorization_header returns
        Base64 part of the Authorization header for a Basic Authentication:
        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header doesn’t start by Basic
        (with a space at the end)
        Otherwise, return the value after Basic (after the space)
        You can assume authorization_header contains only one Basic """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, 
                                           base64_authorization_header:
                                               str) -> str:
        """ returns decoded value of a Base64 str base64_authorization_header:
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header is not a valid Base64 
        - you can use try/except
        Otherwise, return the decoded value as UTF8 string 
        - you can use decode('utf-8')"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base_encode = base64_authorization_header.encode('utf-8')
            base_decode = b64decode(base_encode)
            decode_value = base_decode.decode('utf-8')
            return decode_value
        except Exception:
            return None
