import pyperclip

def set_clipboard(text):
    statement = "Setting clipboard to: "+text
    pyperclip.copy(text)
def get_clipboard(text):
    statement=pyperclip.paste()
# clipboard made