#!/usr/bin/env python3
""" BasicAuth Module """
from .auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ returns the decoded value of base64 string """
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_header = base64_authorization_header.encode('utf-8')
            return base64.decodebytes(decoded_header).decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ extract username and password from decoded header """
        if not decoded_base64_authorization_header or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ":" not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(":")
        return (email, password)
