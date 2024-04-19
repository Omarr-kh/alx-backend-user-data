#!/usr/bin/env python3
""" Session Auth module """
from .auth import Auth
from uuid import uuid4
from models.user import User

class SessionAuth(Auth):
    """ SessionAuth Class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session id for a user id """
        if user_id and isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        else:
            return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ retreive session_id for a user_id """
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a user based on a cookie value """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
