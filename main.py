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
                    print('dictionary ')
                    print()
                    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{t}')
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

                    
                    
                    elif gen_ai_installed:
                        os.system('cls')
                        print('ai')
                        print()
                        print(t)
                        response = model.generate_content("explain this word or sentence to me "+t)
                        print(response.text)

                    pyperclip.copy('')


                prev = t
    except:
        pass