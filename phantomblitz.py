import argparse,time
import os,subprocess
from socket import *
from modules.auto_type import s_print
from modules.phantomblitz_listener import phantomblitz_listen
from modules.phantomblitz_builder import phantomblitz_build
# colors
NONE = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
clear_screen()
# logo 
s_print('''
                                               '''+RED+''' DISCLAIMER '''+NONE+MAGENTA+'''
By using this tool, you agree to the terms and conditions [./terms-and-conditions.md] outlined above and acknowledge that any misuse of this tool is strictly prohibited.'''
+NONE     )
time.sleep(2)
clear_screen()
def intro():
    s_print(f'''{NONE}{BLUE}
            ,%*                                                                 
             #%%%%,                                                             
             ,%%%%%%#,                                                          
              #%%%%%%%%%%,                                                      
              /%%%%%%%%%%%%%,                                                   
               %%%%%%%%%%%%%%%%#.                 %#                            
               %%%%%%%%%%%%%%%%%%%%/                #%%#                        
                ,%%%%%%%%%%%%%%%%%%%%%(.         .#%%%%%%%%(                    
                    (%%%%%%%%%%%%%%%%%%%%%*   /%%%%%%%%%%%%%%%%(                
                       (#%%%%%%%%%%%%%%%%%%%%%%%%%%%%(    /%%%%%(               
                    (*    ,#%%%%%%%%%%%%%%%%%%%%%%%    /%%%%%%%%%,              
                    /%%%(     /%%%%%%%%%%%%%%%%%%%%  ./(#%%%%%%%%%%,            
                    ,%%%%%%#.    ,%%%%%%%%%%%%%%%%%.            ,%%%.           
                     %%%%%%%%%%,     #%%%%%%%%%%%%%.              (%.           
                     /%%%%%%%%%%%%#.    .#%%%%%%%%%.                            
                         #%%%%%%%%%%%(   *%%%%%%%%*                             
                            ,#%%%%%%%#   *%%%%#,                                
                               #%%%%%#   *%#     (%(                            
                               #%%%%%#        (%%%%(                            
                               #%%%%%#    ,%%%%%%%#.                            
                               #%%%%%# /%%%%%%%%,                               
                               #%%%%%%%%%%%%(.                                  
                               #%%%%%%%%%%*                                     
                               #%%%%%%#.                                        
                               #%%%%*                                           
                               ##,                                              {NONE}
                
                     
                        Developer: Dev. Gautam Kumar {RED}
''')
parser = argparse.ArgumentParser()        
parser.add_argument("-m", "--mode", type=str, help="Which mode or function to execute: build or listen")
parser.add_argument("-lh","--lhost",type=str, help="LHOST")
parser.add_argument("-lp","--lport",type=int, help="LPORT")
parser.add_argument("-o","--output",type=str, help="Specify Output file for the payload file name")
parser.add_argument("-c","--command",type=str, help="Command to execute after connection initialization")
args = parser.parse_args()
lhost = args.lhost
lport = args.lport
filename = args.output
if args.mode == "build":
    intro()
    time.sleep(1)
    phantomblitz_build(lhost,lport,filename)
elif args.mode == "listen":
    intro()
    time.sleep(1)
    print(phantomblitz_listen(lhost,lport))
else:
    intro()
    print(
        '''
        usage: PhantomBlitz.py [-h] [-m MODE] [-lh LHOST] [-lp LPORT]

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Which mode or function to execute: build or listen
  -lh LHOST, --lhost LHOST
                        LHOST
  -lp LPORT, --lport LPORT
                        LPORT
  -o  output, --output Output
                        Specify Output file for the payload file name {NONE}
    ''')
