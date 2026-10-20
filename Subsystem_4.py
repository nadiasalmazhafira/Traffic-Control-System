# ENG1013 Subsystem 4: Tunnel Height Detection Subsystem. 
# - Uses two ultrasonic sensors (US3, US4) for overheight detection.
# - Controls TL3 traffic light (red + green LEDs).
# - User sets tunnel height limit (default = 4.0 m).
# Created By : Nadia Salma Zhafira
# Created Date: 01/05/2026
# Last Modified Date: 15/05/2026
# Version = '1.5'

import time
from pymata4 import pymata4

# pin setup
us3Trig = 10
us3Echo = 9
us4Trig = 12
us4Echo = 11
tl3Green = 2
tl3Red = 3
wl2Pin = 4

errorMargin = 5.0 
defaultHeightLimit = 40.0 
heightLimit = defaultHeightLimit

# board setup
board = pymata4.Pymata4()

# functions
def setup():
    """
    Initializes the Arduino pins, configures sonar sensors, and sets initial LED states.
    Parameters:
        None
    Returns:
        None
    """
    global heightLimit

    board.set_pin_mode_sonar(us3Trig, us3Echo, timeout = 12000)
    board.set_pin_mode_sonar(us4Trig, us4Echo, timeout = 12000)
    board.set_pin_mode_digital_output(tl3Green)
    board.set_pin_mode_digital_output(tl3Red)
    board.set_pin_mode_digital_output(wl2Pin)

    board.digital_write(tl3Green, 0)
    board.digital_write(tl3Red, 0)
    board.digital_write(wl2Pin, 0)

    print(f"Default height limit: {defaultHeightLimit / 10.0}m")
    user_input = input("Enter overheight limit in meters: ").strip()

    if user_input == "": 
        heightLimit = defaultHeightLimit
    else:
        try:
            entered = float(user_input)
            heightLimit = entered * 10.0
        except ValueError:
            print("Invalid input")

def get_sonar_distance(trig_pin):
    """
    Read distance from a specific ultrasonic sensor.
    Parameters:
        trig_pin (int): The trigger pin of the sonar sensor to read.
    Returns:
        (float): The distance measured by the sensor in cm.
    """
    data = board.sonar_read(trig_pin)
    if data:
        return data[0]
    else:
        return 0

def loop():
    """
    Continuously monitors sensor data to detect overheight vehicles and update lights.
    Parameters:
        None
    Returns:
        None
    """
    try:
        while True:
            dist3 = get_sonar_distance(us3Trig)
            dist4 = get_sonar_distance(us4Trig)
            overheightDetected = False

            if dist3 > 0 and dist4 > 0:
                if abs(dist3 - dist4) <= errorMargin:
                    if dist3 < heightLimit:
                        overheightDetected = True

            if overheightDetected:
                board.digital_write(tl3Green, 0)
                board.digital_write(tl3Red, 1)
                board.digital_write(wl2Pin, 1)
                time.sleep(0.2)
            else:
                board.digital_write(tl3Green, 1)
                board.digital_write(tl3Red, 0)
                board.digital_write(wl2Pin, 0)
                time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nShutting down...")
        board.shutdown()

# main
try:
    setup()
    loop()
except KeyboardInterrupt:
    board.shutdown()
