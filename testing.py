import time
from pynput.keyboard import Key, Controller
import vgamepad as vg


def main():

    #.5 second delay
    time.sleep(3)
    # press the k key
    # with keyboard.press(Key.space):
    #     time.sleep(1)
    #     keyboard.release(Key.space)

    with keyboard.pressed(Key.space):
        # keyboard.press('a')
        # keyboard.release('a')
        time.sleep(1)

def accelerate(keyb):
    keyb.press(Key.space)


def decelerate(keyb):
    keyb.release(Key.space)

def left(keyb):
    keyb.press('a')

def right(keyb):
    keyb.press('d')

def straight(keyb):
    keyb.release('a')
    keyb.release('d')

def brake(keyb):
    keyb.press('s')

if __name__ == '__main__':
    # keyboard = Controller()
    # time.sleep(1)
    # while True:
    #     accelerate(keyboard)
    #     time.sleep(.1)
    #     decelerate(keyboard)
    time.sleep(1)

    import vgamepad as vg

    gamepad = vg.VDS4Gamepad()
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.update()
