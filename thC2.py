import binascii
import _thread
import time
import socket


HOST2 = '10.0.0.2'
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
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			print('Data2:',data2)





# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
