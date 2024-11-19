import os
from speak import speak



def vscode():
    speak ('boss opening vs code for you')
    os.system('cmd /k "code"')


vscode()