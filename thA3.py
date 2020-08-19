#!/user/bin/env python3
#from opcua import Client
import socket
import binascii
import _thread
import time


HOST = '10.0.0.2'
PORT1 = 991
PORT2 = 992

"""
#OPC ACCESS
url = "opc.tcp://127.0.0.1:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=3")
val2 = client.get_node("ns=2;i=4")
val3 = client.get_node("ns=2;i=5")
val4 = client.get_node("ns=2;i=6")
val5 = client.get_node("ns=2;i=7")
val6 = client.get_node("ns=2;i=8")
val7 = client.get_node("ns=2;i=9")
val8 = client.get_node("ns=2;i=10")
val9 = client.get_node("ns=2;i=11")
val10 = client.get_node("ns=2;i=12")
val11 = client.get_node("ns=2;i=13")
val12 = client.get_node("ns=2;i=14")
val13 = client.get_node("ns=2;i=15")
val14 = client.get_node("ns=2;i=16")
"""

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT1))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2
				while a < 6:

					"""
					#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()
					value14 = val14.get_value()
					"""

					time.sleep(1)

					#covert inetger to string
					value = value+1
					stringd = str(value)

					#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)

					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT2))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				while b < 6:
					data2 = conn2.recv(1024)
					print('Data2:',data2)



# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass