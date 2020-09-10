#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Srep  8 16:48:03 2020

@author: eumin
"""

import pyautogui
import time
import smtplib
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login("sender email", "sender password")





# Click on browser window
x = 200
y = 200
pyautogui.click(x, y)

# Loop
while True:
    # Refresh
    pyautogui.hotkey('command', 'r')
    
    # check for Add button
    if pyautogui.locateOnScreen("add.png", grayscale=True, confidence=.9) != None:
        conn.sendmail("sender email", "receiver email", "Subject: Class Open\n\n")
    else:
        print('none')
    time.sleep(15)
    
    
conn.quit()
