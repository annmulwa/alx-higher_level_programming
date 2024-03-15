#!/usr/bin/python3
'''
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
'''
import MySQLdb
import sys


if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
