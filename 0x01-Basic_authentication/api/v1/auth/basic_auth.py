#!/usr/bin/env python3
""" Basic Auth module to handle API authentication """
from api.v1.auth.auth import Auth


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
