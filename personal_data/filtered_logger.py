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
