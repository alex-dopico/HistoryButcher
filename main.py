"""
Main entry point for HistoryButcher
"""
from history_operations import secure_history


def main():
    secure_history.secure_user_history()


if __name__ == '__main__':
    main()
