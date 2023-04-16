import subprocess
import time
def analyze_lan_traffic(delay,filename):
    statement = 'Starting Trace Capture...'
    subprocess.run(['netsh', 'trace', 'start', 'capture=yes', 'tracefile='+filename], capture_output=True)
    time.sleep(delay)
    statement = 'Stopping Trace...'
    subprocess.run(['netsh', 'trace', 'stop'], capture_output=True)
    return statement