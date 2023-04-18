#!/usr/bin/python3
'''This script lists the states starting with upper N from the database hbtn_0c_0_usa'''

import MySQLdb
import sys

if __name__ == '__main__':
    '''connect to db here'''
    db = MySQLdb.connect(host = 'localhost',
                         port = 3306,
                         user = sys.argv[1],
                         passwd = sys.argv[2],
                         db = sys.argv[3],
        )