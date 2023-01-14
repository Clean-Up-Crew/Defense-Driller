'''
A simple program that trains reactions to certain mixups. Used best in training mode.
Player must be on the left side for this to work.
'''

import time
#import pyautogui
import keyboard
import random
import vgamepad as vg

def shago(rand_num):
    '''
    This function does the high-low mix for Shadow Jago.
    It alternates between D+MK and F+HK.
    '''
    if rand_num == 1:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.right_trigger_float(value_float=1.0)
        gamepad.update()
        time.sleep(0.25)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.right_trigger_float(value_float=0)
        gamepad.update()
    else:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        time.sleep(0.25)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
    
def shoto(rand_num):
    '''
    This function does the high-low mix for Jago, Fulgore, Spinal, and Rash.
    It alternates between D+MK and B+HP.
    '''
    if rand_num == 1:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        gamepad.update()
        time.sleep(0.25)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        gamepad.update()
    else:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        time.sleep(0.25)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()

gamepad = vg.VX360Gamepad()

response = 0
while response == 0:
    print("Type 1 for Shadow Jago, 2 for all the characters with B+HP overheads.")
    try:
        response = int(input())
    except:
        print("Try again.")

# Prototype for the time being
# We need to know which keys to press, but it'll follow simple logic
time.sleep(5)

rand_num = 0
while(True):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    gamepad.update()
    rand_num = random.randint(1, 3)
    if response == 1:
        shago(rand_num)
    else:
        shoto(rand_num)