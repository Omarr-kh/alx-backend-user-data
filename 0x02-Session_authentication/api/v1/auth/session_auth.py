#!/usr/bin/env python3
""" Session Auth module """
from .auth import Auth
from uuid import uuid4


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
