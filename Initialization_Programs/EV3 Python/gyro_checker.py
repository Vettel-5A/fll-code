from pybricks.hubs import EV3Brick
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
Gyro = GyroSensor(Port.S1)

# Clear Screen
ev3.screen.clear()

# Reads and writes angle into a variable (measure_1)
wait(500)
measure_1 = Gyro.angle()

# Waits 2 seconds, then reads and writes angle into a 
# second variable (measure 2)
wait(2000)
measure_2 = Gyro.angle()

# Compares values of both variables.
if measure_1 == measure_2:
    # If values are equal, the brick will give multiple 
    # signals indicating the Gyro Sensor is ready to use.
    ev3.screen.draw_text(0, 0, "Gyro OK")
    ev3.light.on(Color.GREEN)
    ev3.speaker.play_notes(['A5/2,', 'A5/2'])
else:
    # Otherwise the brick will give multiple signals
    # indicating the Gyro Sensor must be plugged in again.
    ev3.screen.draw_text(0, 0, "Gyro BAD")
    ev3.light.on(Color.RED)
    ev3.speaker.play_notes(['A5/2,', 'E4/2xw'])

    

