#!/usr/bin/python3

import MySQLdb
from sys import argv
import sys

'''This code will get all states from the database hbtn_0e_0_usa'''

if __name__ == "__main__":
    '''First line of code will connect to MySQLserver running on localhost on port 3306 '''
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    '''Second line of code will help you navigate on the database '''
    cur = db.cursor
    '''This line will help you to pin point what to execute'''
    cur.execute("SELECT *FROM states ORDER by id ASC")
    '''This function allows for all the information to be fetched and placed in rows'''
    rows = cur.fetchall()
    '''This line is a for loop that will run for rows'''
    for rows in rows:
        '''print the rows'''
        print(rows)
    '''close the cursor'''
    cur.close()
    '''close the db'''
    db.close()