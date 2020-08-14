#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#  SQL lite - fully functional, cross-platform, database system
# suitable for many online and mobile applications.
import sqlite3

# every database engine has its own interface, its own requirements
# no single interface


def main():
    print('connect')
    # connects to DB
    db = sqlite3.connect('.\\15_DatabaseAPI\\db-api.db')    # returns DB handle
    cur = db.cursor()
    print('create')

    # execute SQLs
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)

    # commit SQL
    print('commit')
    db.commit()

    # count SQL
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')

    # for multiple select
    for row in cur.execute("SELECT * FROM test"):
        print(row)

    # closing
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()


if __name__ == '__main__':
    main()
