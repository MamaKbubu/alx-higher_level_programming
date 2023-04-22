#!/usr/bin/python3

import MySQLdb
from sys import argv


'''This code will get all states from the database hbtn_0e_0_usa'''

if __name__ == "__main__":
    '''First line of code will connect to MySQLserver running on localhost on port 3306 '''
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    '''Second line of code will create a cursor object'''
    db_cursor = db_connect.cursor()
    '''Third line of code will execute a query'''  
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    '''Fourth line of code will fetch all rows from the last executed query'''
    rows_select = db_cursor.fetchall()
    '''Fifth line of code will print all rows'''
    for row in rows_select:
        print(row)