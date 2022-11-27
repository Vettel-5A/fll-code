from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

# Creating instances
ev3 = EV3Brick()
gyro = GyroSensor(Port.S1)

# Sets the speed of the motors
d_motor1 = Motor(Port.B)
d_motor2 = Motor(Port.C)
d_motor1.run(1)
d_motor2.run(1)

# Code time

while True:
    if gyro.angle() 
    
