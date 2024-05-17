#!/usr/bin/env python3
""" Implement a hash_password function that expects one string argument
name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).
Implement an is_valid function that expects 2 arguments and returns a boolean
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password, which is a byte string
    Use the bcrypt package to perform the hashing (with hashpw)
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ is_valid function that expects 2 arguments and returns a boolean
    Arguments:
    hashed_password: bytes type
    password: string type
    Use bcrypt to validate that the provided password matches hashed password
    """
    return bcrypt.checkpw(bytes(password, "ascii"), hashed_password)
