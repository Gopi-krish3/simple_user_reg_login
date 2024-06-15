import sqlite3 as sl
import os

if not os.path.isdir('databases'):
    os.mkdir('databases')

try:
    con=sl.connect('databases/db.sqlite3')
    cur=con.cursor()
    print('connection created..')
except con.Error:
    print("error...")
else:
    cur.execute('create table if not exists login_auth(username varchar(20) primary key, password varchar(70))')
finally:
    cur.close()
    con.commit()
    con.close()
    print('connection established and closed successfully...')