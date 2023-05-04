#!/usr/bin/env python

import time
import os
from datetime import datetime
from pynput.mouse import Controller as MouseController

mouse = MouseController()

def intro():
    print("   __   ____  _________________  _______  _______   ___  __  ____________")
    print("  / /  / __ \/ ___/_  __/  _/  |/  / __/ / __/ _ | / _ \/  |/  / __/ _  / ")
    print(" / /__/ /_/ / (_ / / / _/ // /|_/ / _/  / _// __ |/ , _/ /|_/ / _// , _/")
    print("/____/\____/\___/ /_/ /___/_/  /_/___/ /_/ /_/ |_/_/|_/_/  /_/___/_/|_| ")
    print("\n\n")
    print("   Created by : humartin")
    print("alias to launch it : logfarm")

def get_now_timestamp():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


intro()
lastSavePosition = (0, 0)
try:
    time.sleep(1)
    while 1:
        print(get_now_timestamp(), 'How many hour do you wanna farm ?')
        farming = input('')
        try:
            number = int(farming)
            break
        except ValueError:
            print("Invalid number")
    print(get_now_timestamp(), "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(get_now_timestamp(), "X       Put the video in fullscreen,      X")
    print(get_now_timestamp(), "X    lower the contrast to the maximum,   X")
    print(get_now_timestamp(), "X   disconnect your mouse and keyboard    X")
    print(get_now_timestamp(), "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print(get_now_timestamp(), "You're going to farm ", number, 'hours.\n')
    time.sleep(5)
    print(get_now_timestamp(), 'Starting browser')
    time.sleep(1)
    os.system('open -a Firefox https://www.youtube.com/watch?v=AjWfY7SnMBI')
    time.sleep(5)
    print(get_now_timestamp(), 'Starting logtime farming in 20 seconds')
    time.sleep(20)
    print(get_now_timestamp(), 'Farming logtime during', number, 'hours.')
    start = datetime.now()
    flag = 1
    farmingSeconds = 0
    farmingMinutes = 0
    farmingHours = 0

    # timeToFarm in second
    timeToFarm = int(farming) * 3600

    while farmingSeconds < timeToFarm:
        currentPosition = mouse.position
        if flag == 1:
            lastSavePosition = currentPosition
            flag = 0
        is_user_away = currentPosition == lastSavePosition
        now = datetime.now()

        if is_user_away:
            currentPosition = mouse.position

        if not is_user_away:
            print('Someone is here')
            if farmingHours > 0:
                farmingMinutes = farmingHours % 60
                farmingSeconds = farmingMinutes % 60
                print('Time farmed : ', farmingHours, 'hours,', farmingMinutes, 'minutes,', farmingSeconds, 'seconds')
            elif farmingMinutes > 0:
                farmingSeconds = farmingMinutes % 60
                print('Time farmed : ', farmingMinutes, 'minutes,', farmingSeconds, 'seconds')
            elif farmingSeconds > 0:
                print('Time farmed : ', farmingSeconds, 'seconds')
            os.system('pmset displaysleepnow')
            break
        
        lastSavePosition = currentPosition

        delta = now - start
        farmingSeconds = int(delta.total_seconds())
        if farmingSeconds >= 60 and farmingSeconds % 60 == 0:
            farmingMinutes = farmingSeconds / 60
        if farmingMinutes >= 60 and farmingMinutes % 60 == 0:
            farmingHours = farmingMinutes / 60
    print('\nLogtime farm will end soon')
    os.system('pmset displaysleepnow')

except KeyboardInterrupt:
    print("\nLogtime is interrupted")
    exit()
