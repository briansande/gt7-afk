import vgamepad as vg
import time

# load gamepad
gamepad = vg.VDS4Gamepad()
gamepad.update()
time.sleep(1)

button_delay = .3




def restart():
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
    gamepad.update()
    time.sleep(1)

    gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)



    gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
    gamepad.update()
    time.sleep(button_delay)

    gamepad.reset()
    gamepad.update()

    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()
    time.sleep(1)

    gamepad.reset()
    gamepad.update()

def accelerate():
    gamepad.right_joystick_float(0,1)
    gamepad.update()

def boost():
    #press square
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.update()

def hug_right():
    gamepad.left_joystick_float(.3,0)
    gamepad.update()






def press_down():
    print("Down")
    gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
    gamepad.update()
    time.sleep(button_delay)
    gamepad.directional_pad(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    gamepad.update()

def press_right():
    print("Right")
    gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
    gamepad.update()
    time.sleep(button_delay)
    gamepad.directional_pad(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
    gamepad.update()

def press_x():
    print("X")
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()
    time.sleep(button_delay)
    gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()


def start_from_world_circuit():
    print("Starting from world circuit")
    # Press down, right x 6, then x twice -- starting from the world circuit menu
    press_down()

    for _ in range(6):
        press_right()
        time.sleep(2)

    for _ in range(2):
        press_x()
        time.sleep(2)

    # delay for load time
    print("Loading track")

    time.sleep(13)

    for _ in range(2):
        press_x()
        time.sleep(2)

def race():
    print("Starting race")
    accelerate()
    boost()
    hug_right()

    # # Sleep for 4 minutes 30 seconds
    # time.sleep(280)

    #sleep for 280 seconds, print out time every 10 seconds
    for i in range(29):
        time.sleep(10)
        print(str((i+1)*10) + " seconds have elapsed")

    gamepad.reset()
    gamepad.update()


def exit_race():
    print("Exiting race")
    #navigate menu to restart
    # Press x to leave the timing screen
    # Press x to leave the champ screen
    # Press x 2 times to leave the points screen
    # Press x 2 times to exit rewards screen
        # If first of the day, you need to press x to collect daily reward
        # Not currently coded.
    # Press x again to leave rewards
    # Press x twice to exit replay screen

    print("Leaving timing screen")
    for _ in range(9):
        press_x()
        time.sleep(2)
    time.sleep(4)

    # Press right on dpad then x to go to next race
    press_right()
    time.sleep(2)
    press_x()
    time.sleep(2)

    # Track loading time
    print("Loading track")
    time.sleep(15)

    # Press x to enter race
    press_x()
    time.sleep(2)

    # Press right 4 times to hover exit, then hit x twice to exit the series.
    for _ in range(4):
        press_right()
        time.sleep(2)

    press_x()
    time.sleep(2)

    press_x()
    time.sleep(2)


    print("Loading back to main menu")
    time.sleep(15)


#if name is main
if __name__ == '__main__':
    iterations = 1
    start = time.time()

    while True:
        start_from_world_circuit()
        race()
        exit_race()

        print("------------------")
        print("Iteration " + str(iterations) + " complete")
        payout = 52500 * iterations
        print("Total Payout: " + str(payout))
        print("Time Elapsed: " + str( (time.time() - start) / 3600 )) + " hours"
        # Calculate credits per hour
        print("Credits per hour: " + str(int(payout / ((time.time() - start) / 3600))))

        print("------------------")
        iterations += 1







