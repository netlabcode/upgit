from opcua import Client
import time
import sqlite3
from sqlite3 import Error
import datetime



def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file, timeout=10)

	except Error as e:
		print(e)

	return conn


# OPC Connection
url = "opc.tcp://127.0.0.1:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("client connected")

#Database Connection
datafile = "test.db"
con = create_connection(datafile)
c = con.cursor()


i = 1
while i < 2:
	val0 = client.get_node("ns=2;i=2")
	val1 = client.get_node("ns=2;i=3")

	value0 = val0.get_value()
	value1 = val1.get_value()

	#Get Value
	datet = datetime.datetime.now()
	var1 = 20.5
	var2 = 9.765
	print(datet)

	#convert
	stringd = str(value0)+"-"+str(value1)
	data1 = stringd.encode()
	data2 = data1.decode("utf-8")
	a,b = data2.split("-",1)
	print(b)
	print(type(stringd))
	print(type(data1))
	print(type(data2))

	c.execute("INSERT INTO substation3(xtime, value1, value2) VALUES (?,?,?)",(datet,a,b))
	con.commit()

	i = i+1
	time.sleep(1)




"""
for row in c.execute('SELECT * FROM substation3'):
    print (row)
"""

con.close()
client.disconnect()