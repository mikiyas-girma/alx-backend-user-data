#!/usr/bin/env python3
"""
module for filtering data
"""
import re


def filter_datum(fields, redaction, message, separator):
    """should use a regex to replace occurrences of certain field values
    and  returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
