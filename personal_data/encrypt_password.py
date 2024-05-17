#!/usr/bin/env python3
""" Implement a hash_password function that expects one string argument
name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).
"""


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password, which is a byte string
    Use the bcrypt package to perform the hashing (with hashpw)
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
