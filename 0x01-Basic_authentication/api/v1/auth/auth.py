#!/usr/bin/env python3
""" Authentication module. """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if path is not in the excluded list """
        if path and excluded_paths:
            if path.endswith('/'):
                alter = path[:-1]
            else:
                alter = path + '/'
            if path in excluded_paths or alter in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ returns None for now """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None for now """
        return None
