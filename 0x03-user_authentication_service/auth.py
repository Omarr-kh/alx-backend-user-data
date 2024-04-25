#!/usr/bin/env python3
""" Module for Authentication """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ hashes a password and return it in bytes """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
