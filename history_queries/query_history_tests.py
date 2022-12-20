"""
TEST SUITE FOR query_history_test.py
    TODO: fix the 'today' design error
"""
import getpass
import unittest
from sqlite3 import Connection
from db_connection.Connection import *
import query_history
import time


def get_conn():
    current_user = getpass.getuser()
    today = time.strftime("_%Y_%m_%d")
    database = f'{current_user}{today}_history'
    connection = Connection.connect(database)

    return connection


class QueryHistoryTests(unittest.TestCase):
    """Tests for query_history.py"""

    def test_connection_object_created(self):
        connection = get_conn()
        self.assertIsInstance(connection, Connection)

    def test_query_is_not_null(self):
        connection = get_conn()
        query_result = query_history.select_all_records(connection)
        self.assertIs(query_result, None)


if __name__ == '__main__':
    unittest.main()
