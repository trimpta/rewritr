import pyperclip
import time
import requests
import json

while True:
    time.sleep(0.1)
    t =pyperclip.paste() 
    if t:
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{t}')
        defintion = json.loads(requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{t}').text)
        print(defintion['meanings'])
        pyperclip.copy('')
    
