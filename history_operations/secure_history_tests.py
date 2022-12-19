import unittest
from secure_history import secure_user_history


class SecureHistoryTestCase(unittest.TestCase):
    """Tests for 'secure_history.py'."""

    def test_copy_user_history(self):
        history_secured = secure_user_history()
        self.assertEqual(history_secured, True)


if __name__ == '__main__':
    unittest.main()
