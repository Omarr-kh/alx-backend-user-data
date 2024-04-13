#!/usr/bin/env python3
""" Regex to hide personal fields """
import re
from typing import List
import logging

PII_FIELDS = ("password", "ip", "ssn", "phone", "name")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """

        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
) -> str:
    """ filter personal fields """
    for field in fields:
        pattern = fr'{field}=([^{separator}]+){separator}'

        message = re.sub(pattern, fr'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """ returns a logger """

    # create a logger 'user_data' only logs INFO
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # redactingForm as stream handler
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
