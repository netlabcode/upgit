import binascii
import _thread
import time
import socket


HOST = '127.0.0.1'
PORT1 = 991
PORT2 = 992
PORTS1 = 881
PORTS2 = 882

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST, PORT1))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
			s1.bind((HOST,PORTS1))
			s1.listen()
			conn1, addr = s1.accept()
			with conn1:
				print('S1 from:',addr)
				while True:
					a = 1
					while a < 6:
						#recive data from server A
						data1 = sc1.recv(1024)
						#send data to server C
						conn1.sendall(data1)
						print('S1:',data1)


def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2:
		sc2.connect((HOST, PORT2))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
			s2.bind((HOST,PORTS2))
			s2.listen()
			conn2, addr = s2.accept()
			with conn2:
				print('S2 from:',addr)
				while True:
					i = 1
					while i < 6:
						#recive data from server A
						#data2 = sc2.recv(1024)
						data2 = conn2.recv(1024)
						print('S2:',data2)
						#send data to server C
						#conn2.sendall(data2)
						sc2.sendall(data2)

						

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
