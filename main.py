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
    model = genai.configure(api_key=key.API_KEY)#type your api key
    model = genai.GenerativeModel("gemini-1.5-flash")
    gen_ai_installed = True

except:
    gen_ai_installed = False

def print_with_newlines(text):
    words = text.split()  # Split text into words
    new_text = []
    word_count = 0

    for word in words:
        new_text.append(word)
        word_count += 1

        # Check if it's the 10th word and there's no newline in the last words
        if word_count % 10 == 0 and '\n' not in word:
            new_text.append('\n')

    # Join and print the resulting text
    print(" ".join(new_text))


prev = None

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128




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
                        response = model.generate_content(f"Rewrite the following to make it around {int(len(t.split())*0.7)} words long ensuring the main content and structure(line numbers if exists in given text) is still there: {t}")
                        time_saved = int(len(response.text.split())/23.9676884839*60)

                        print(f"+++++{len(t.split())}--{time_saved//60}:{time_saved%60}-->{len(response.text.split())}++++++")
                        print_with_newlines(response.text)

                    pyperclip.copy('')


                prev = t
    except:
        pass