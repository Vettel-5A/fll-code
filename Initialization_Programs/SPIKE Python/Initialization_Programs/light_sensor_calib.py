from spike import PrimeHub, LightMatrix, Button, ColorSensor, App
from spike.control import wait_until

#Create your objects here.
hub = PrimeHub()
light_sensor = ColorSensor("E")

hub.light_matrix.write('Black')

# Waits until the right button is pressed
## FOR OPERATOR: Place light sensor on black line before
# pressing the right button
hub.right_button.wait_until_pressed():
    BLACK = light_sensor.get_reflected_light()
    hub.speaker.beep()

# Saves % value of reflection of black line into a constant
## TO TEAM: REMEMBER TO LINK THIS VARIABLE TO YOUR RUN CODE,
## YOU WANT TO MAKE SURE THAT THIS VALUE IS WHAT YOUR CODE
## SHOULD BE USING WHEN USING THE LIGHT SENSOR
hub.light_matrix.write("White")

# Waits until the center button is pressed
## FOR OPERATOR: Place light sensor on white line before
# pressing the center button
hub.right_button.wait_until_pressed()
    WHITE = light_sensor.get_reflected_light()
    hub.speaker.beep()

# Saves % value of reflection of white line into a constant
## TO TEAM: REMEMBER TO LINK THIS VARIABLE TO YOUR RUN CODE,
## YOU WANT TO MAKE SURE THAT THIS VALUE IS WHAT YOUR CODE
## SHOULD BE USING WHEN USING THE LIGHT SENSOR
hub.light_matrix.write("Completed")
