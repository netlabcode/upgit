
import sqlite3

"""
connection = sqlite3.connect('test.db')
cursor = connection.cursor()
#cursor.execute("CREATE TABLE newtable (name TEXT, value1 INTEGER, value2 INTEGER)")
cursor.execute("INSERT INTO newtable VALUES('a','2','3')")
cursor.execute("INSERT INTO newtable VALUES('b','2','3')")

print(connection.total_changes)

rows = cursor.execute("SELECT name, value1, value2 FROM newtable").fetchall()
print(rows)

cursor.close()
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

data_person_name = [('Michael', 'Fox'),
                    ('Adam', 'Miller'),
                    ('Andrew', 'Peck'),
                    ('James', 'Shroyer'),
                    ('Eric', 'Burger')]

con = sqlite3.connect("test.db", timeout=10)
c = con.cursor()

"""
c.execute('''CREATE TABLE q1_person_name
             (name_id INTEGER PRIMARY KEY,
              first_name varchar(20) NOT NULL,
              last_name varchar(20) NOT NULL)''')

c.executemany('INSERT INTO q1_person_name(first_name, last_name) VALUES (?,?)', data_person_name)
"""
c.execute("INSERT INTO q1_person_name(first_name, last_name) VALUES ('alfax','betax')")
#c.execute("INSERT INTO q1_person_name VALUES(5, '2','3')")

for row in c.execute('SELECT * FROM q1_person_name'):
    print (row)
con.commit()

con.close()