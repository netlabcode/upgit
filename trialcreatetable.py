
import sqlite3

con = sqlite3.connect("test.db", timeout=10)
c = con.cursor()

c.execute('''CREATE TABLE substation3
             (id INTEGER PRIMARY KEY,
              xtime DATETIME,
              value1 DECIMAL(20) NOT NULL,
              value2 DECIMAL(20) NOT NULL)''')

con.commit()
con.close()