#!/usr/bin/env python3
""" Basic Auth module to handle API authentication """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Authentication class """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Basic Base64 part
        returns the Base64 part from the passed authorization
        header
        """
        if authorization_header is None or \
            type(authorization_header) is not str or \
                not authorization_header.startswith("Basic "):
            return None

        base64 = authorization_header.split(" ")[1]
        return base64

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ returns the decoded value of the Base64 String
            base64_authorization_header
        """
        if base64_authorization_header is None or \
            not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header, validate=True)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
            returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        username, password = decoded_base64_authorization_header.split(':')
        return (username, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
            returns the User instance based on his email and password.
        """
        if not user_email or not user_pwd or \
            not isinstance(user_email, str) or \
                not isinstance(user_pwd, str):

            return None

        if not User.search({"email": user_email}):
            return None
        user = User.search({"email": user_email})
        if len(user) == 0:
            return None
        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
            returns the user from a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            base64_auth_header = self.extract_base64_authorization_header(auth_header)
            if base64_auth_header is not None:
                decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
                if decoded_auth_header is not None:
                    user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)
                    if user_email is not None:
                        return self.user_object_from_credentials(user_email, user_pwd)
        return
