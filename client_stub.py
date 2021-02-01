try:
	fin = open('client.py',"r")
	function_calls = (fin.read()).split("\n") #list
	fin.close()
	
except:
	print("No server file found")

from socket import *

HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 7000        # The port used by the client
with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	y=str(function_calls).encode()
	mysocket.sendall(y) 
	mysocket.close()

#Now function calls answers are to be received
HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 9000        # The port used by the client

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

   
client_connection, client_address = server_socket.accept()
data=client_connection.recv(4096).decode('utf-8')
answers=eval(data)
mysocket.close()

server_socket.close()

print("-----------")
for i in answers:
	print(i)
print("-----------")