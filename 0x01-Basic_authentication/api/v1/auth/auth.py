#!/usr/bin/env python3
"""" Auth module to handle API authentication """
from flask import Flask, request
from typing import List, TypeVar
import re


class Auth:
    """
    template for all authentication system in this app
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ checks paths that require auth """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            pattern = excluded_path[:-1]
            if re.match(pattern, path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """validate all requests to secure the API """
        if request is None:
            return None
        if 'Authorization' not in request.headers.keys():
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user in the flask request object"""
        return None
