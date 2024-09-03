#!/usr/bin/env python3
""" Basic Auth module to handle API authentication """
from api.v1.auth.auth import Auth
import base64


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
