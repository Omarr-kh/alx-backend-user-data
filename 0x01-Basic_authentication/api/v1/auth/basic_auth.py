#!/usr/bin/env python3
""" BasicAuth Module """
from .auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth class """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ extract base64 authorization header """
        if not authorization_header or \
            not isinstance(authorization_header, str) or \
                not authorization_header.startswith('Basic '):
            return None
        else:
            encoded64 = authorization_header[6:]
            return encoded64
