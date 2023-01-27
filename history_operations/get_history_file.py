
class LocalHistoryFile:

    def __init__(self):
        self.local_history_file = self.get_local_history_file()

    @classmethod
    def get_local_history_file(cls):
        file = '../resources.py'
        return file
