#!/usr/bin/python3
"""connect"""


import sys
import MySQLdb

if __name__== "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3], charset="utf-8")
    c = conn.cursor()
    c.execute(
            "SELECT * from states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    conn.close()

