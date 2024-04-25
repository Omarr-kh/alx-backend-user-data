#!/usr/bin/env python3
""" Module for Authentication """
import bcrypt
from db import DB


def _hash_password(password: str) -> bytes:
    """ hashes a password and return it in bytes """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a user and store it in the db """
        try:
            if self._db.find_user_by(email=email, password=password):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
