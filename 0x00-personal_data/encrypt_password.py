#!/usr/bin/env python3
""" encrypting passwords. """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password using a random salt """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hash_password: bytes, password: str) -> bool:
    """ validate the provided password matches the hashed password """
    return bcrypt.checkpw(password.encode("utf-8"), hash_password)
