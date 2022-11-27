from spike import PrimeHub, ColorSensor, App, Motor, MotorPair

# NOTE TO USER: You may need to change the speed of the motors depending on how you implement this into your runs
# NOTE TO USER: We use 50 as the threshold for reflective light intensity for sensing a line.
    # You might need to change this value if you use our calibration program.
hub = PrimeHub()
right_sensor = ColorSensor('E')
left_sensor = ColorSensor('F')

# Assumming A is left motor and B is right motor. 
motor_pair = MotorPair('B', 'A')
left_motor = Motor('A')
right_motor = Motor('B')

# Starts both motors to move straight
motor_pair.start(steering=0)


# Checks to see if any color sensor senses line
while right_sensor.get_reflected_light() > 50 and left_sensor.get_reflected_light() > 50:
    # If right sensor senses line, then right motor stops and left motor continues to turn until left sensor senses line.
    if right_sensor.get_reflected_light() < 50:
        right_motor.stop()
        while left_sensor.get_reflected_light() > 50:
            left_motor.start()
        left_motor.stop()

    # If left sensor senses line, then left motor stops and right motor continues to turn until right sensor senses line.
    elif left_sensor.get_reflected_light() < 50:
        left_motor.stop()
        while right_sensor.get_reflected_light() > 50:
            right_motor.start()
        right_motor.stop()    


    


