#!/usr/bin/env python3
""" Session Authentication module """
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Session authentication class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session id for the user id passed
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        if session_id is None:
            return None
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes a user's session or
            logout
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if not self.user_id_for_session_id(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True
