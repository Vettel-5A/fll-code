from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog
from tkinter import *
from tkinter import messagebox
from Robot_Inputs import RobotData

def update_values():
    

def change_to_widget():
    if var1.get() == 1:
        if button_pressed == 1:
            widget1.config(image=gyro_window)
            Slabel1.config(highlightbackground="black")
        elif button_pressed == 2:
            widget2.config(image=gyro_window)
            Slabel2.config(highlightbackground="black")
        elif button_pressed == 3:
            widget3.config(image=gyro_window)
            Slabel3.config(highlightbackground="black")
        elif button_pressed == 4:
            widget4.config(image=gyro_window)
            Slabel4.config(highlightbackground="black")
    elif var2.get() == 1:
        if button_pressed == 1:
            widget1.config(image=touch_window)
            Slabel1.config(highlightbackground="black")
        elif button_pressed == 2:
            widget2.config(image=touch_window)
            Slabel2.config(highlightbackground="black")
        elif button_pressed == 3:
            widget3.config(image=touch_window)
            Slabel3.config(highlightbackground="black")
        elif button_pressed == 4:
            widget4.config(image=touch_window)
            Slabel4.config(highlightbackground="black")
    elif var3.get() == 1:
        if button_pressed == 1:
            widget1.config(image=light_window)
            Slabel1.config(highlightbackground="black")
        elif button_pressed == 2:
            widget2.config(image=light_window)
            Slabel2.config(highlightbackground="black")
        elif button_pressed == 3:
            widget3.config(image=light_window)
            Slabel3.config(highlightbackground="black")
        elif button_pressed == 4:
            widget4.config(image=light_window)
            Slabel4.config(highlightbackground="black")
    elif var4.get() == 1:
        if button_pressed == 1:
            widget1.config(image=us_window)
            Slabel1.config(highlightbackground="black")
        elif button_pressed == 2:
            widget2.config(image=us_window)
            Slabel2.config(highlightbackground="black")
        elif button_pressed == 3:
            widget3.config(image=us_window)
            Slabel3.config(highlightbackground="black")
        elif button_pressed == 4:
            widget4.config(image=us_window)
            Slabel4.config(highlightbackground="black")

def choose_motor_window():
    print("hello")
#
#
def choose_sensor_window(button):
    widget = Menubutton()
    menu = Menu(widget)
    global var1, var2, var3, var4, button_pressed
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    button_pressed = button
    if button_pressed == 1:
        Slabel1.config(highlightbackground="white")
    elif button_pressed == 2:
        Slabel2.config(highlightbackground="white")
    elif button_pressed == 3:
        Slabel3.config(highlightbackground="white")
    elif button_pressed == 4:
        Slabel4.config(highlightbackground="white")
    menu.add_checkbutton(label="Gyro", variable=var1,command=change_to_widget)
    menu.add_checkbutton(label="Touch", variable=var2, command=change_to_widget)
    menu.add_checkbutton(label="Color", variable=var3, command=change_to_widget)
    menu.add_checkbutton(label="Ultrasonic", variable=var4, command=change_to_widget)
    widget["menu"] = menu
    widget.config(text="Choose Widget")
    widget.grid(column=4, row=0)

window = Tk()
robodata = RobotData()

window.title("EV3 Dashboard")
window.config(padx=0, pady=0, bg="silver")
window.minsize(width=1400, height=800)

dashboard = Canvas(window, width=1400, height=800,  highlightthickness=0)
dashboard.place()

# Port Labels
MPort = Label(text="Motor Port:", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0)
MPort.grid(column=0, row=1)

SPort = Label(text="Sensor Port:", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0)
SPort.grid(column=0, row=3)

# Motor Port Labels
label1 = Button(text="A", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0, highlightbackground="black",)
label1.grid(column=1, row=1, pady=25)

label2 = Button(text="B", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0, highlightbackground="black",)
label2.grid(column=2, row=1, pady=25)

label3 = Button(text="C", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0, highlightbackground="black",)
label3.grid(column=3, row=1, pady=25)

label4 = Button(text="D", font=("Ariel", 20, "bold"), bg="silver", highlightthickness=0, highlightbackground="black",)
label4.grid(column=4, row=1, pady=25)

# Motor Widget Labels

motor_window = PhotoImage(file="Screen Shot 2022-10-08 at 4.21.57 PM.png")
motor_1 = Label(image=motor_window, bg="silver", highlightthickness=0)
motor_1.grid(column=1, row=2, padx=0)

motor_2 = Label(image=motor_window, bg="silver", highlightthickness=0)
motor_2.grid(column=2, row=2, padx=0)

motor_3 = Label(image=motor_window, bg="silver", highlightthickness=0)
motor_3.grid(column=3, row=2, padx=0)

motor_4 = Label(image=motor_window, bg="silver", highlightthickness=0)
motor_4.grid(column=4, row=2, padx=0)

# Motor Data Labels

motor_1_value = Label(text="0", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
motor_1_value.grid(column=1, row=2, padx=10)

motor_2_value = Label(text="0", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
motor_2_value.grid(column=2, row=2, padx=10)

motor_3_value = Label(text="0", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
motor_3_value.grid(column=3, row=2, padx=10)

motor_4_value = Label(text="0", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
motor_4_value.grid(column=4, row=2, padx=10)

# Sensor Port Labels

Slabel1 = Button(text="S1", font=("Ariel", 20, "bold"), highlightcolor="silver", background="gray", highlightbackground="black", highlightthickness=0, command=lambda state=1: choose_sensor_window(state))
Slabel1.grid(column=1, row=3)

Slabel2 = Button(text="S2", font=("Ariel", 20, "bold"), highlightcolor="silver", background="gray", highlightbackground="black", highlightthickness=0, command=lambda state=2: choose_sensor_window(state))
Slabel2.grid(column=2, row=3)

Slabel3 = Button(text="S3", font=("Ariel", 20, "bold"), highlightcolor="silver", background="gray", highlightbackground="black", highlightthickness=0, command=lambda state=3: choose_sensor_window(state))
Slabel3.grid(column=3, row=3)

Slabel4 = Button(text="S4", font=("Ariel", 20, "bold"), highlightcolor="silver", background="gray", highlightbackground="black", highlightthickness=0, command=lambda state=4: choose_sensor_window(state))
Slabel4.grid(column=4, row=3)

# Define Widgets
gyro_window = PhotoImage(file="Imagegyro.png")
touch_window = PhotoImage(file="Imagetouch.png")
light_window = PhotoImage(file="Imagelight.png")
us_window = PhotoImage(file="Imageus.png")

# Sensor Widget Labels

widget1 = Label(image=gyro_window, bg="silver", highlightthickness=0)
widget1.grid(column=1, row=4, padx=0, pady=70)

widget2 = Label(image=touch_window, bg="silver", highlightthickness=0)
widget2.grid(column=2, row=4, padx=0, pady=70)

widget3 = Label(image=light_window, bg="silver", highlightthickness=0)
widget3.grid(column=3, row=4, padx=0, pady=70)

widget4 = Label(image=us_window, bg="silver", highlightthickness=0)
widget4.grid(column=4, row=4, padx=0, pady=70)

#Sensor Data

sensor_1_value = Label(text=f"{robotdata.gyrosensor}", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
sensor_1_value.grid(column=1, row=4, padx=10)

sensor_2_value = Label(text=f"{robotdata.touchsensor}", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
sensor_2_value.grid(column=2, row=4, padx=10)

sensor_3_value = Label(text=f"{robotdata.colorsensor}", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
sensor_3_value.grid(column=3, row=4, padx=10)

sensor_4_value = Label(text=f"{robotdata.ussensor}", fg="black", font=("Ariel", 20, "bold"), bg="white", highlightthickness=0)
sensor_4_value.grid(column=4, row=4, padx=10)

title = Label(text="EV3 FLL Dashboard", background="#1caafc", font=("Ariel", 35, "bold"), justify="center", anchor="center", width=58, height=2)
title.grid(column=0, row=0, columnspan=7)

window.mainloop()



