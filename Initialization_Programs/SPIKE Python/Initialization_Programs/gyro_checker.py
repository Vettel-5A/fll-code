from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

# Reads and writes angle into a variable (measure_1)
wait_for_seconds(0.5)
measure_1 = hub.get_yaw_angle()

# Waits 2 seconds, then reads and writes angle into a
# second variable (measure 2)
wait_for_seconds(2000)
measure_2 = hub.get_yaw_angle()

# Compares values of both variables.
if measure_1 == measure_2:
    # If values are equal, the brick will give multiple
    # signals indicating the Gyro Sensor is ready to use.
    hub.light_matrix.write("Gyro OK")
    hub.status_light.on('green')
    hub.speaker.beep()

else:
    # Otherwise the brick will give multiple signals
    # indicating the Gyro Sensor must be plugged in again.
    hub.light_matrix.write("Gyro BAD")
    hub.status_light.on('red')
