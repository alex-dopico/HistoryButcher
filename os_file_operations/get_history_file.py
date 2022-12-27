from get_os_info import *


class LocalHistoryFile:

    local_history_file = None

    def __init__(self):
        self.local_history_file = self.get_local_history_file()

    @staticmethod
    def get_os():
        current_os = get_current_os()
        return current_os

    @staticmethod
    def get_current_user():
        current_user = get_current_user()
        return current_user

    @classmethod
    def get_local_history_file(cls):
        file = '..\\resources.py'
        return file
