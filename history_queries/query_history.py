"""
A collection of queries to the history file.
    TODO: write views in this file, query them in a separate file
    TODO: write stats and show them --> pyplot
    TODO: fix visit duration format
"""
from db_connection import Connection
import resources
import time


def select_all_records():
    today = time.strftime("_%Y_%m_%d")
    database = f'{resources.get_os_user()}{today}_history'
    conn = Connection.connect(database)
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT(u.title), SUM(v.visit_duration)\n"
                "FROM urls AS u\n"
                "INNER JOIN visits AS v\n"
                "ON u.id = v.url\n"
                "WHERE v.visit_duration > 0\n"
                "GROUP BY u.title")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
        print(row[1])

    return rows
