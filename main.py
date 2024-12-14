import win32api
import pyautogui
import time
import pyperclip
import os
import requests
import json

prev = None

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128




from os import system


while True:
    try:
        a = win32api.GetKeyState(0x01)

        if a != state_left:  # Button state changed
            state_left = a


            if a>=0:
                with pyautogui.hold('ctrl'):
                    pyautogui.press('c')
                t = pyperclip.paste()
                
                if t and t!= prev:
                    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{t}')
                    os.system('cls')
                    print(t)
                    if response.status_code == 200:
                        meanings = json.loads(response.text)[0]['meanings']
                        for i in meanings:
                            print('part of speech:',i['partOfSpeech'])
                            for j in i['definitions']:
                                print('defintion:',j['definition'])
                                if 'example' in j:
                                    print('example:',j['example'])
                                print()
                            print()

                    pyperclip.copy('')
                    
                prev = t
    except:
        pass