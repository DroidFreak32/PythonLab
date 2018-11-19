# p28_server.py
import socket
import sys


HOST = socket.gethostname()
PORT = 9999

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(5)

print("Listening ...")

while True:
    conn, addr = soc.accept()
    print("[+] Client connected: ", addr)

    # content will be put in recv.txt
    file = open("recv.txt", "wb")
    while True:
        # get file bytes
        data = conn.recv(4096)
        if not data:
            break
        # write bytes on file
        file.write(data)
    file.close()
    print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")

#############################################
