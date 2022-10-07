from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog
import run1
import run2
import run3
import run4
import run5
import run6
import run7
import run8

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create instances here.
ev3 = EV3Brick()

button_pressed = False
ev3.screen.clear()

# Write your program here.
if len(buttons.pressed()) == 1:
    if buttons.pressed() == UP:
        run1()
    elif buttons.pressed() == RIGHT:
        run2()
    elif buttons.pressed() == LEFT:
        run3()
    elif buttons.pressed() == DOWN:
        run4()
    elif buttons.pressed() == CENTER:
        screen.change_screen()
    
    else:




    
