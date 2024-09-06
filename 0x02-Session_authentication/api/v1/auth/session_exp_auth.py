#!/usr/bin/env python3
""" module for adding expiration time to
    session id
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ session expiration class """
    def __init__(self):
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION", "0"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """creates a new session for passed user
            by its user id
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns user_id for the given session id"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        session_dictionary = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dictionary['user_id']
        if 'created_at' not in session_dictionary.keys():
            return None
        curr_time = datetime.now()
        time_span = timedelta(seconds=self.session_duration)
        expire_at = session_dictionary['created_at'] + time_span
        if expire_at < curr_time:
            return None
        return session_dictionary['user_id']
