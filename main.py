"""
Main entry point for HistoryButcher
"""
from history_operations import secure_history
from html_builder import create_html_history


if __name__ == '__main__':
    secure_history.secure_user_history()
    create_html_history.build_html_file()
    