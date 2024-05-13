#!/usr/bin/env python3
""" function filter_datum returns the log message obfuscated:
Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all
fields in the log line (message)
The function should use a regex to replace occurrences of certain field values
filter_datum should be less than 5 lines long and use re.sub to perform the
substitution with a single regex."""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ The function should use a regex to replace occurrences of certain
    field values filter_datum should be less than 5 lines long and use re.sub
    to perform the substitution with a single regex."""
    log = message.split(separator)
    for field in fields:
        for i in range(len(log)):
            log[i] = re.sub(field + '=.*', field + '=' + redaction, log[i])
    return separator.join(log)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Update the class to accept a list of strings fields constructor
        argument. """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Implement the format method to filter values in incoming log
        records using filter_datum. Values for fields in fields should be
        filtered.
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
