"""
A collection of queries to the history file.
    TODO: write views in this file, query them in a separate file
    TODO: write stats and show them --> pyplot
    TODO: fix visit duration format
    TODO: fix the 'today' design error
"""
from db_connection.Connection import Connection
from os_file_operations.get_os_info import get_current_user
import resources
import time


def select_all_records():
    today = time.strftime("_%Y_%m_%d")
    current_user = get_current_user()
    database = f'{current_user}{today}_history'
    conn = Connection(database)
    cur = conn.connection.cursor()

    cur.execute("SELECT DISTINCT(u.title), SUM(v.visit_duration)\n"
                "FROM urls AS u\n"
                "INNER JOIN visits AS v\n"
                "ON u.id = v.url\n"
                "WHERE v.visit_duration > 0\n"
                "GROUP BY u.title")

    rows = cur.fetchall()

    """ debug purpose
        for row in rows:
        print(row[0])
        print(row[1])
        """

    return rows
