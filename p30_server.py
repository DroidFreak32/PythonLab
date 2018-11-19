# p28_server.py
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen(1)

while True:
    c,addr=s.accept()
    exp=str(c.recv(1024))
    print("Recieved: ",exp)
    n1=""
    n2=""
    for i in range(len(exp)):
        if exp[i].isdigit():
            n1=n1+exp[i]
        elif exp[i]=='+' or exp[i]=='-' or exp[i]=='*' or exp[i]=='/':
            break;
    n1=int(n1)
    op=exp[i]
    for j in range(i+1,len(exp)):
        if exp[j].isdigit():
            n2=n2+exp[j]
        else:
            break;
    n2=int(n2)
    if op=="+":
        res=n1+n2
    elif op=="-":
        res=n1-n2
    elif op=="*":
        res=n1*n2
    elif op=="/":
        res=n1//n2
    
    c.send(str(res).encode('ascii'))
    c.close()

#############################################
