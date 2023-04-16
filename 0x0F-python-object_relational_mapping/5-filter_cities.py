#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    state = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                INNER JOIN states ON cities.state_id \
                = states.id WHERE states.name = %s \
                ORDER BY cities.id ASC", (state, ))
    rows = cur.fetchall()
    print(*[row[0] for row in rows], sep=", ")
    cur.close()
    conn.close()
