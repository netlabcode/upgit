import binascii
import _thread
import time
import socket


HOST = '127.0.0.1'
PORT1 = 881
PORT2 = 882

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((HOST, PORT1))
		i = 1
		while i < 6:
			#recive data from server
			data1 = s1.recv(1024)
			print('Data1:',data1)

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((HOST, PORT2))
		a = 1
		value2 = 0
		while a < 6:
			#recive data from server
			time.sleep(1)

			value2 = value2+5
			stringd2 = str(value2)
			data2 = stringd2.encode()

			s2.sendall(data2)

			#data2 = s2.recv(1024)
			#print('Data2:',data2)




# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
