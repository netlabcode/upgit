import binascii
import _thread
import time
import socket


HOST2 = '10.1.0.31'
PORT1 = 881
PORT2 = 883

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((HOST2, PORT1))
		i = 1
		while i < 6:
			#recive data from server
			data1 = s1.recv(1024)
			print('Data1:',data1)

# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((HOST2, PORT2))
		x = 1
		value=0
		while x < 6:

			time.sleep(1)

			#covert inetger to string
			value = value+5
			stringd = str(value)

			#stringd = str(value1)+"-"+str(value2)+"-"+str(value3)

			#convert string to bytes data
			data2 = stringd.encode()

			s2.sendall(data2)






# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
