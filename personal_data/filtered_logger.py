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
import os
import mysql.connector


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


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
""" Create a tuple PII_FIELDS constant at the root of the module containing
the fields from user_data.csv that are considered PII. PII_FIELDS can contain
only 5 fields"""


def get_logger() -> logging.Logger:
    """ Implement a get_logger function that takes no arguments and
    returns a logging.Logger object.
    The logger should be named "user_data" and only log up to logging.INFO
    level. It should not propagate messages to other loggers. It should
    have a StreamHandler with RedactingFormatter as formatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Implement a get_db function that returns a connector to the database
    (mysql.connector.connection.MySQLConnection object).
    Use the os module to obtain credentials from the environment
    Use the module mysql-connector-python to connect to the MySQL database
    (pip3 install mysql-connector-python)"""
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))

def main():
    """ The function will obtain a database connection using get_db and
    retrieve all rows in the users table and display each row under a
    filtered format """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        record = ''
        i = 0
        for header in cursor.column_names:
            record += f"{header}={row[i]};"
            i = i + 1
        log_record = logging.LogRecord("user_data", logging.INFO, None, None,
                                       record, None, None)
        formatter = RedactingFormatter(fields=PII_FIELDS)
        print(formatter.format(log_record))
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()