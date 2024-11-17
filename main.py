import pyperclip
import time
import requests
import json
import os
import pyautogui

prev = None
while True:
    time.sleep(0.1)
    with pyautogui.hold('ctrl'):
        pyautogui.press('c')
    t =pyperclip.paste() 
    
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