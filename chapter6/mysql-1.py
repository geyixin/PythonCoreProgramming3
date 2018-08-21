import sqlite3
cxn = sqlite3.connect('BBBB')
cur = cxn.cursor()
cur.execute('CREATE TABLE BBBB(login VARCHAR(8), userid INTEGER)')
cur.execute('INSERT INTO BBBB VALUES("john", 100)')
cur.execute('INSERT INTO BBBB VALUES("jane", 110)')
cur.execute('SELECT * FROM BBBB')
for eachUser in cur.fetchall():
    print(eachUser)

# ('john', 100)
# ('jane', 110)

cur.execute('DROP TABLE BBBB')
cur.close()
cxn.commit()
cxn.close()