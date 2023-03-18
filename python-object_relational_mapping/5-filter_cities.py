#!/usr/bin/python3
"""Script that lists all cities from a state received as an argument"""

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
    query = "SELECT cities.name FROM cities JOIN states \
        ON cities.state_id = states.id WHERE states.name \
        LIKE %s ORDER BY cities.id"
    cur.execute(query, (matchname,))
    query_rows = cur.fetchall()

    count = 0
    for row in query_rows:
        print(row[0], end="")
        count += 1
        if count < len(query_rows):
            print(", ", end="")
    print()
    cur.close()
    conn.close()
