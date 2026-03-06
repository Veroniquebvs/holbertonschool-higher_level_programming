#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and
lists all cities of that state"""

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

    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM cities INNER JOIN states ON "
        "cities.state_id = states.id WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name_searched,)
    )

    rows = cur.fetchall()

    cities = []
    for row in rows:
        cities.append(row[0])
    print(", ".join(cities))

    cur.close()
    db.close()
