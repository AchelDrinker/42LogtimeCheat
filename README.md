# LOGTIME - FARMER

This program will lock screen your computer at 42 if someone moves the mouse.  
The program is set to lock your screen after 5 hours if nobody touches it. You can change this value by changing timeToFarm.

After launching it, the only thing to do is to put the video in fullscreen.

To launch it everywhere, use the alias below after restart your terminal.

##### Run

```
logfarm
```

## Installation

Copy and paste all the following lines in your terminal.

```
cd && git clone https://github.com/AchelDrinker/logtime-farmer.git logtime-farmer
pip3 install pynput
cd logtime-farmer/src && chmod 777 install.sh && ./install.sh
python3 logtime-farmer.py
```

