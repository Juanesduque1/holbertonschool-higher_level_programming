#!/usr/bin/python3
"""Script that lists all states starting with 'N' from a database"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchname = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s"
    cur.execute(query, (matchname,))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
