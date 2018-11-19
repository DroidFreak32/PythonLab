# p28_client.py
"""
Write a Client/Server Socket program to demonstrate the file transfer operation using Python Programming.
"""
# client

import socket
import sys


HOST = socket.gethostname()
PORT = 9999

soc = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
soc.connect((HOST, PORT))
print("[+] Connected with Server")

# get file name to send
file_name = input("Enter file name to send : ")
# open file
try:
    file = open(file_name, "rb")
    # send file
    print("[+] Sending file...")
    data = file.read()
    soc.sendall(data)

    # close connection
    soc.close()
    file.close()
    print("[-] Disconnected")

except FileNotFoundError:
    print("Error : file not found")

#############################################
