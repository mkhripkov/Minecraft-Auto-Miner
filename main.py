import pyautogui as pag
import pydirectinput as di
from time import sleep

# Moves The Character
# x = attack
# c = place
def move_character(key_press, duration, action='walking'):
    di.keyDown(key_press)
    if action == 'walking':
        print('Walking')
    elif action == 'attack':
        di.keyDown('x')
    
    sleep(duration)
    di.keyUp('x')
    di.keyUp(key_press)

def locate_lava():
    position = pag.locateCenterOnScreen('images/lava_texture.jpeg', confidence=0.4)
    if position is None:
        return False
    else:
        # Move the character backwards to avoid burning in lava
        move_character('s', 2)
        print('Found Lava!!!')
        return True

# Start The Game
sleep(3)
di.press('esc')

duration = 10
while duration != 0:
    # Chck if there is lava
    if not locate_lava():
        move_character('w', 2, 'attack')
    else:
        break
    duration -= 1
    print('Time Remaining:', duration)
