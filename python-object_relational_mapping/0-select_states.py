#!/usr/bin/python3
"""orm"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = mysql.connector.connect(host = "localhost", port = "3306", user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    conn.close()