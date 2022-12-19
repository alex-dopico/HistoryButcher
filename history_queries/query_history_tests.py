import unittest
from sqlite3 import Connection
import query_history
import resources
import time


class QueryHistoryTests(unittest.TestCase):
    """Tests for query_history.py"""

    def test_connection_object_created(self):
        current_user = resources.get_os_user()
        today = time.strftime("_%Y_%m_%d")
        database = f'{current_user}{today}_history'
        connection = query_history.create_connection(database)
        self.assertIsInstance(connection, Connection)

    def test_query_is_not_null(self):
        current_user = resources.get_os_user()
        today = time.strftime("_%Y_%m_%d")
        database = f'{current_user}{today}_history'
        connection = query_history.create_connection(database)
        query_result = query_history.select_all_records(connection)
        self.assertIs(query_result, None)


if __name__ == '__main__':
    unittest.main()
