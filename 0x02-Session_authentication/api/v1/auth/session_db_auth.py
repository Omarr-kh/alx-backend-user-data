#!/usr/bin/env python3
""" Session DB Auth module """
from .session_exp_auth import SessionExpAuth
from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Session DB Auth class """

    def create_session(self, user_id=None):
        """ creates and stores a session id for a user """
        session_id = super().create_session(user_id)
        if session_id:
            kwargs = {
                "user_id": user_id,
                "session_id": session_id,
            }
            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns a user id by session id """
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(sessions) <= 0:
            return None
        time_now = datetime.now()
        time_span = timedelta(seconds=self.session_duration)
        expiry_time = sessions[0].created_at + time_span
        if expiry_time < time_now:
            return None
        return sessions[0].user_id

    def destroy_session(self, request=None):
        """ destroys a session """
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(sessions) <= 0:
            return False
        sessions[0].remove()
        return True
