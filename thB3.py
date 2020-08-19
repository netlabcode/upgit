import binascii
import _thread
import time
import socket


HOST1 = '192.168.1.100'
HOST2 = '172.16.0.100'
PORT1 = 991
PORT2 = 992
PORTS1 = 881
PORTS2 = 883

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
			s1.bind((HOST2,PORTS1))
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

# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2:
		sc2.connect((HOST1, PORT2))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
			s2.bind((HOST2,PORTS2))
			s2.listen()
			conn2, addr2 = s2.accept()
			with conn2:
				print('S2 from:',addr2)
				while True:
					b = 1
					while b < 6:
						#recive data from server A
						data2 = conn2.recv(1024)
						#send data to server C
						sc2.sendall(data2)
						print('S2:',data2)

						

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
