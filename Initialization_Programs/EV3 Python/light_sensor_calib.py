from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
light_sensor = ColorSensor(Port.S2)

# Clears screen 
ev3.screen.clear()

ev3.screen.draw_text(0, 0, "Measure Black")

# Waits until the center button is pressed
## FOR OPERATOR: Place light sensor on black line before 
# pressing the center button
while Button.CENTER not in buttons.pressed():
    wait(1)

ev3.speaker.beep()

# Saves % value of reflection of black line into a constant
## TO TEAM: REMEMBER TO LINK THIS VARIABLE TO YOUR RUN CODE, 
## YOU WANT TO MAKE SURE THAT THIS VALUE IS WHAT YOUR CODE 
## SHOULD BE USING WHEN USING THE LIGHT SENSOR
BLACK = light_sensor.reflection()

ev3.screen.draw_text(0, 0, "Measure White")

# Waits until the center button is pressed
## FOR OPERATOR: Place light sensor on white line before 
# pressing the center button
while Button.CENTER not in buttons.pressed():
    wait(1)

ev3.speaker.beep()

# Saves % value of reflection of white line into a constant
## TO TEAM: REMEMBER TO LINK THIS VARIABLE TO YOUR RUN CODE, 
## YOU WANT TO MAKE SURE THAT THIS VALUE IS WHAT YOUR CODE 
## SHOULD BE USING WHEN USING THE LIGHT SENSOR
WHITE = light_sensor.reflection()

ev3.speaker.beep()
ev3.screen.draw_text(0, 0, "Calibration Completed")




    
