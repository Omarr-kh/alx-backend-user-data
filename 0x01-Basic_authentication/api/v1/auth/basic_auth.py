#!/usr/bin/env python3
""" BasicAuth Module """
from .auth import Auth
import base64
import binascii
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password """
        if not isinstance(user_email, str) or \
                not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})[0]
        except BaseException:
            return None

        if user.is_valid_password(user_pwd):
            return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth = self.extract_base64_authorization_header(auth_header)
        decoded_auth = self.decode_base64_authorization_header(b64_auth)
        email, password = self.extract_user_credentials(decoded_auth)
        return self.user_object_from_credentials(email, password)
