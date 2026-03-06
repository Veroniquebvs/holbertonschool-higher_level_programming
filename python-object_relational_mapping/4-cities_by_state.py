#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the
states table"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c "
                "INNER JOIN states AS s ON s.id = c.state_id "
                "ORDER BY c.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
