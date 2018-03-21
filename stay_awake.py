import pyautogui
from pyautogui import position as position
from pyautogui import moveRel as moveRel
from pyautogui import moveTo as moveTo
from time import sleep as sleep
from random import randint as randint

pyautogui.FAILSAFE = False


old_pos = position()

ticker = 0

while True:
    
    sleep(1)

    new_pos = position()

    if old_pos != new_pos:
        sleep(100)
        old_pos = position()
        pass

    if old_pos == new_pos:
        while ticker <=2:
            x = randint(-10,10)
            y = randint(-10,10)
            a = str(old_pos).split(', ')[0]
            a = a.replace('(','')
            b = str(old_pos).split(', ')[1]
            b = b.replace(')','')
            x = (x+int(a))
            y = (y+int(b))
            moveTo(int(x),int(y))
            sleep(.001)
            moveTo(int(a),int(b))
            ticker += 1
        x = randint(-10,10)
        y = randint(-10,10)
        a = str(old_pos).split(', ')[0]
        a = a.replace('(','')
        b = str(old_pos).split(', ')[1]
        b = b.replace(')','')
        x = (x+int(a))
        y = (y+int(b))
        moveTo(int(x),int(y))
        sleep(.001)
        moveTo(int(a),int(b))
        ticker = 0
        old_pos = position()
        pass
    else:
        pass