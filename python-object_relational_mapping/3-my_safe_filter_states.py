#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states table"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    sql = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")

    cursor.execute(sql, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
