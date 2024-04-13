#!/usr/bin/env python3
""" Regex to hide personal fields """
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """ filter personal fields """
    for field in fields:
        pattern = fr'{field}=([^{separator}]+){separator}'

        message = re.sub(pattern, fr'{field}={redaction}{separator}', message)
    return message
