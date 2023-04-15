#!/usr/bin/python3
""" A script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cur = conn.cursor()
    check = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC", (check, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
