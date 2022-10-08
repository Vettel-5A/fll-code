from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog

# Create objects:

# Assuming we are using ports B and C for the drive motors:
motor1 = Motor(B)
motor2 = Motor(C)

# Assuming we are using port 1 for the Gyro Sensor:
gyrosensor = GyroSensor(S1)

# Assuming we are using port 2 for the Touch Sensor:
touchsensor = TouchSensor(S2)

# Assuming we are using port 3 for the Color Sensor:
colorsensor = ColorSensor(S3)

# Assuming we are using port 4 for the Ultrasonic Sensor:
ussensor = UltrasonicSensor(S4)

# FOR OPERATOR: Begin program after robot is placed on field.

# Reset sensor + motor values
motor1.reset_angle(0)
motor2.reset_angle(0)

gyrosensor.reset_angle(0)

for x in range():
    motor1_val = motor1.angle()
    motor2_val = motor2.angle()
    gyro_val = gyrosensor.angle()
    reflection_val = colorsensor.reflection()
    us_val = ussensor.distance
    touch_val = touchsensor.pressed()
    



    


