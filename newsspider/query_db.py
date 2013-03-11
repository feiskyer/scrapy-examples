#!/usr/bin/python
#coding: utf-8

def query():
    import MySQLdb
    conn = MySQLdb.connect(host='localhost', user='root',passwd='feisky',
            db='news' , charset="utf8")
    try:
        cursor = conn.cursor()
        cursor.execute("select * from news")
        data =  cursor.fetchall()
    finally:
        conn.close()

    for d in data:
        print '%-60s %-30s' % (d[1],d[2])

if __name__ == '__main__':
    query()
