#!/usr/bin/env python3
"""" Auth module to handle API authentication """
from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """
    template for all authentication system in this app
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns paths that require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ returns flask request object """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user in the flask request object"""
        return None
