#!/usr/bin/env python3
"""
module for encrypting and decrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """encrypts the given password and
        returns the hashed password
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if the given password is equivalent
        to the hashed_password
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
