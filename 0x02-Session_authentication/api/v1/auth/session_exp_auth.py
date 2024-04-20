#!/usr/bin/env python3
""" Session auth with expiration date """
from .session_auth import SessionAuth
from flask import request
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Auth with expiration date class """

    def __init__(self):
        """ """
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ create a session id from user id """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now(),
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ return a user id by session id """
        if session_id in self.user_id_by_session_id:
            session_data = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_data["user_id"]
            if not session_data.get("created_at"):
                return None
            time_now = datetime.now()
            time_span = timedelta(seconds=self.session_duration)
            expiry_time = session_dict.get('created_at') + time_span
            if expiry_time < time_now:
                return None
            return session_data.get("user_id")
