# LOGTIME - FARMER

This program will lock screen you computer at 42 if someone moves the mouse.  
The program is set to lock your screen after 5 hours if nobody touches it. You can change this value by changing timeToFarm.

After launching it, the only thing to do is to put the video in fullscreen.

To launch it everywhere, use the alias below after restart your terminal.

##### Run

```
logfarm
```

## Manual installation

```
cd && git clone https://github.com/AchelDrinker/logtime-farmer.git logtime-farmer && cd logtime-farmer
pip3 install pynput
alias logfarm='python3 ~/$HOME/logtime-farmer/src/logtime-farmer.py'
python3 src/logtime-farmer.py
```

