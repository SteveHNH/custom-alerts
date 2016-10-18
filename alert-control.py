#!/usr/bin/python

from __future__ import print_function
import os
import requests
import json

ACCESS_TOKEN = 'access token here'

'''
ALERT POST CODE
===============
'''

url = 'http://www.twitchalerts.com/api/v1.0/alerts'

payload = {
    "access_token": ACCESS_TOKEN,
    "duration": "5",
    "type": "subscription",
    "special_text_color": "#ff0000"
}

def alert(mod):

    if mod == 'assist':
        payload['message'] = "Thanks for the *assist!*"
        payload['image_href'] = 'placeholder'
        payload['sound_href'] = 'placeholder'
    if mod == 'victory':
        payload['message'] = "*VICTORY!*"
        payload['image_href'] = 'placeholder'
        payload['sound_href'] = 'placeholder'
    if mod == 'fail':
        payload['message'] = "*TOTAL FAIL!*"
        payload['image_href'] = 'placeholder'
        payload['sound_href'] = 'placeholder'
    if mod == 'tip':
        payload['message'] = "*U DA BES!*"
        payload['image_href'] = 'placeholder'
        payload['sound_href'] = 'placeholder'
    if mod == 'success':
        payload['message'] = "*SUCCESS!*"
        payload['image_href'] = 'placeholder'
        payload['sound_href'] = 'placeholder'

    session = requests.Session()
    response = session.post(url, data=payload)

'''
CONTROL PANEL INTERFACE CODE
============================
'''

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

STARTED = True
while STARTED:
    print('''
        
             Alert Control Panel
             ===================

1. Assist
2. Victory
3. Fail
4. Tip Jar
5. Random Success
6. Quit

Choose: ''', end='')
    choice = raw_input()
    if choice == '1':
        alert('assist')
        clearScreen()
    elif choice == '2':
        alert('victory')
        clearScreen()
    elif choice == '3':
        alert('fail')
        clearScreen()
    elif choice == '4':
        alert('tip')
        clearScreen()
    elif choice == '5':
        alert('success')
        clearScreen()
    elif choice == '6':
        STARTED = False
    else:
        print('Not a valid choice')
        clearScreen()
