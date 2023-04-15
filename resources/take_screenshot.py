import datetime
import pyautogui
global interval
interval = 60
def generate_file_name():
    generation_time = datetime.datetime.now()
    filename = generation_time.strftime("Screenshot_%Y-%m-%d_%H-%M-%S")
    return filename
def take_screenshot():
    statement = 'Taking screenshot...'
    pyautogui.screenshot().save(generate_file_name() + '.png')
    statement = 'Screenshot saved!'
take_screenshot()