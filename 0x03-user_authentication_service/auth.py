#!/usr/bin/env python3
"""
module for auth service
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user  and returns a User object
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashedpw = _hash_password(password)
            user = self._db.add_user(email, hashedpw)
            return user
        raise ValueError(f'User {email} already exists')


def _hash_password(password: str) -> bytes:
    """returns the salted hash of the input password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash
