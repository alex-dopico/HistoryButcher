"""
Describes a connection to the database file
and returns a connection object
    TODO: accept various db engines in order to expand number of browsers
    TODO: expand constructor to load database options / parameters
    TODO: expand damage control operations through various types of error
"""
import sqlite3
from sqlite3 import Error
from os import error


class Connection:

    """ describes a connection """
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.connection = self.__connect(db_file_path)

    def get_connection(self):
        if self.connection is None:
            print('This is not possible; anyway, restart')
            return None

        return self.connection

    @classmethod
    def __connect(cls, db_file_path):
        conn = None

        # DAMAGE CONTROL #####################
        # Try to manage db and io errors:
        try:
            conn = sqlite3.connect(db_file_path)
        except Error as sql_err:
            print('Not possible to connect')
            print(sql_err)
        except error as io_err:
            print(io_err)
        ######################################

        return conn
