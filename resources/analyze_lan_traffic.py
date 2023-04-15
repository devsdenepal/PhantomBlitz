import os
import time
def analyze_lan_traffic(delay):
    statement = 'Starting Trace Capture...'
    os.system('netsh trace start capture=yes tracefile=tracefile.etl')
    time.sleep(delay)
    statement = 'Stopping Trace...'
    os.system('netsh trace stop')
