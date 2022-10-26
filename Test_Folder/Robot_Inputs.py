from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog

class RobotData

    def __init__(self):
        super().__init__()
        self.d_motor1 = Motor(B)
        self.d_motor2 = Motor(C)
        # Assuming we are using port 1 for the Gyro Sensor:
        self.gyrosensor = GyroSensor(S1)
        # Assuming we are using port 2 for the Touch Sensor:
        self.touchsensor = TouchSensor(S2)
        # Assuming we are using port 3 for the Color Sensor:
        self.colorsensor = ColorSensor(S3)
        # Assuming we are using port 4 for the Ultrasonic Sensor:
        self.ussensor = UltrasonicSensor(S4)
        # Reset Data Variables
        motor1_val = 0
        motor2_val = 0
        gyro_val = 0
        reflection_val = 0
        us_val = 0
        touch_val = 0

    def reset():
        d_motor1.reset_angle(0)
        d_motor2.reset_angle(0)
        gyrosensor.reset_angle(0)

    def get_values():
        for x in range():
            motor1_val = motor1.angle()
            motor2_val = motor2.angle()
            gyro_val = gyrosensor.angle()
            reflection_val = colorsensor.reflection()
            us_val = ussensor.distance()
            touch_val = touchsensor.pressed()
    



    


