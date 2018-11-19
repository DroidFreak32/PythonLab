# p28_client.py
"""
Write a client/server program where the client program takes the expression (n1 op n2 where n1 and n2 are operands and op can be +,-,*,/ ) from the user and sends the expression to the server program. The server program performs the specified operation and sends the result to the client program and displays it on the user’s console.
"""
# client

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.connect((host,port))
msg="112/22"
s.send(msg.encode('ascii'))
ans=s.recv(1024)
print(ans.decode('ascii'))

#############################################
