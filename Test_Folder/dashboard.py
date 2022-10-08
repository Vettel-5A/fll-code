from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("EV3 Dashboard")
window.config(padx=500, pady=400)

canvas = Canvas(width=200, height=200)
# Add a team logo to the top of the dashboard:
    # logo_img = PhotoImage(file="logo.png")
    # canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)



