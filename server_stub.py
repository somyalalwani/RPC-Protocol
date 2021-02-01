import server
"""
class Proxy:
    
    def __init__(self,name):
    	self.name=name
    #def __call__(self,*args):
"""

try:
	fin = open('server.py',"r")
	content = (fin.read()).split("\n")
	fin.close()
	#print(content)

except:
	print("No server file found")

fileinfo={}

i=0
for i in range(len(content)):
	if(content[i].startswith("def")):
		i1=content[i].index("(")
		i2=content[i].index(")")
		function_name = str(content[i])[4:i1]
		function_parameter = str(content[i])[i1+1:i2]
		no_of_parameter=len(function_parameter.split(","))
		fileinfo[function_name]=[no_of_parameter]

final_ans=[]

import socket
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

#while True:    
client_connection, client_address = server_socket.accept()
data = client_connection.recv(1024).decode('utf-8')
data=eval(data)
#data is function calls recvd

funcDetails=dict()
funct_name=None
#print("$$$$$$$1$$$$$$")
for i in data:
	j=i
	i1 = str(i).find('(')
	i2 = i1 + str(i)[i1+1:].find('(')
	if(i1>i2):
		funct_name=str(i)[:i1]
	else:
		funct_name=str(i)[i1+1:i2+1]
	i3 = str(i).index(')')
	
	if(i2!=-1):
		if(i2+1<i3):
			p=str(i)[i2+1:i3]
	else:
		if(i1+1<i3):
			p=str(i)[i1+1:i3]
		else:
			p=""
	p=p.strip("(")
	args=p.split(",")

	if funct_name in fileinfo.keys():
		methodToCall = getattr(server,funct_name) #add
		if(args!=[""]):
			ans = methodToCall(*args)
		else:
			ans=methodToCall()
		final_ans.append(ans) #list
	else :
		final_ans.append("Function doesn't exist")
	
y=(str(final_ans)).encode()
client_connection.send(y)

client_connection.close()

# Close socket
server_socket.close()