"""
Describes a connection to the database file
and returns a connection object
    TODO: expand constructor to load database options / parameters
    TODO: expand damage control operations through various types of error
"""
import sqlite3
from sqlite3 import Error
from os import error


# static method to return connection object
def connect(db_file):
    conn = None

    # DAMAGE CONTROL #####################
    # Try to manage db and io errors:
    try:
        conn = sqlite3.connect(db_file)
    except Error as sql_err:
        print('Not possible to connect')
        print(sql_err)
    except error as io_err:
        print(io_err)
    ######################################

    return conn


class Connection:

    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
