from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog
from runs import run1, run2, run3, run4, run5, run6, run7, run8


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create instances here.
ev3 = EV3Brick()

button_pressed = False
ev3.screen.clear()

# Write your program here.
while not button_pressed:
    if len(buttons.pressed()) == 1:
        if buttons.pressed() == UP:
            # Insert Run 1 run code
        if buttons.pressed() == RIGHT:
            # Insert Run 2 run code
        if buttons.pressed() == LEFT:
            # Insert Run 3 run code
        if buttons.pressed() == DOWN:
            # Insert Run 4 run code
        if buttons.pressed() == CENTER:
            screen.change_screen()
    
    else:




    
