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

            for _path in excluded_paths:
                # if ex_path endswith '*'
                if _path.endswith('*'):
                    if path[:len(_path) - 1] == _path[:-1]:
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """ validate requests """
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None for now """
        return None

    def session_cookie(self, request=None):
        """ return a cookie value from a request """
        if request:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
