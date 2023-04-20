#!/usr/bin/env python

import time
import os
from datetime import datetime, timedelta
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

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
    print(get_now_timestamp(), 'Starting browser')
    os.system('open -a Firefox https://www.youtube.com/watch?v=AjWfY7SnMBI')
    time.sleep(5)
    print(get_now_timestamp(), 'Starting logtime farming in 20 seconds')
    time.sleep(20)
    print(get_now_timestamp(), 'Farming logtime')
    start = datetime.now()
    flag = 1
    farmingSeconds = 0
    farmingMinutes = 0
    farmingHours = 0

    # time is in second
    timeToFarm = 18000

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
            exit()

        lastSavePosition = currentPosition

        delta = now - start
        farmingSeconds = int(delta.total_seconds())
        if farmingSeconds >= 60 and farmingSeconds % 60 == 0:
           farmingMinutes = farmingSeconds / 60
           if farmingMinutes >= 60 and farmingMinutes % 60 == 0:
                farmingHours = farmingMinutes / 60
    print('\nLogtime farm will end soon')
    print('If you want more logtime, set the value in timeToFarm')
    os.system('pmset displaysleepnow')

except KeyboardInterrupt:
    print("\nLogtime is interrupted")
    exit()
