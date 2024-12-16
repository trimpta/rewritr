import win32api
import pyautogui
import time
import pyperclip
import os
import requests
import json
from os import system

try:
    import google.generativeai as genai
    import key
    
    model = genai.configure(api_key=key.api_key)#type your api key
    model = genai.GenerativeModel("gemini-1.5-flash")
    gen_ai_installed = True

except:
    gen_ai_installed = False


prev = None

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

print(gen_ai_installed)



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
                    os.system('cls')
                    print('rewritr ')
                    print()
                    
                    if gen_ai_installed:
                        os.system('cls')
                        print('ai')
                        print()
                        print(t)
                        response = model.generate_content("Rewrite the following to make it shorter ensuring all the content is still there: "+t)
                        print(response.text)

                    pyperclip.copy('')


                prev = t
    except:
        pass