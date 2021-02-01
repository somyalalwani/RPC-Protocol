from socket import *
import pickle
#code with client to get function calls
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7000 #client_stub

# Create socket

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

	# Wait for client connections
client_connection, client_address = server_socket.accept()
    
    # Get the client request
data=client_connection.recv(4096).decode('utf-8') #str

client_connection.close()

	
# Close socket
server_socket.close()

"""///// """
#code with server to compute function
HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 8000        # The port used by the server_stub


with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	
	mysocket.send(data.encode()) 
	
	#answers are to be received here
	
	data=mysocket.recv(4096).decode('utf-8') #string
	mysocket.close()

#now send this data back to client
HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 9000        # The port used by the client_stub

with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	mysocket.sendall(data.encode())
	mysocket.close()

