import unittest
import resources
from Connection import Connection


class ConnectionsTests(unittest.TestCase):
    """Tests for Connection.py"""

    def test_connection_object_created(self):
        database = resources.CHROME_WIN_PATH
        connection = Connection(database)
        self.assertIsInstance(connection, Connection)


if __name__ == '__main__':
    unittest.main()
