#motor_drive

# Import required modules
import tkinter as tk
import sys
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
A0 = 15 # Enable motor_1
D7 = 11 # Clockwise motor_1
D8 = 12 # Counter-clockwise motor_1

# set up GPIO pins
GPIO.setup(A0, GPIO.OUT) # Enable pin for motor
GPIO.setup(D8, GPIO.OUT) # Rotate Counter-clockwise
GPIO.setup(D7, GPIO.OUT) # Rotate Clockwise


def stop_motor():
    GPIO.output(D7, GPIO.LOW)
    GPIO.output(D8, GPIO.LOW)
    GPIO.output(A0, GPIO.LOW)
    print('Motor Stopped ...')

def rotate_clockwise():
    GPIO.output(D7, GPIO.HIGH) # Enabled clockwise
    GPIO.output(D8, GPIO.LOW) # Disabled counter-clockwise
    print('Rotating Clockwise ...')
    
def rotate_counter_clockwise():
    GPIO.output(D7, GPIO.LOW) # Disabled clockwise
    GPIO.output(D8, GPIO.HIGH) # Enabled counter-clockwise
    print('Rotating Counter-clockwise. ..')

def enable_motor():
    GPIO.output(A0, GPIO.HIGH) # Enabled Motor
    print('Motor Enabled ...')
    
def close_all():
    print('Closing Everything')
    GPIO.cleanup()
    sys.exit()
    
#stop_motor()

root = tk.Tk()

logo = tk.PhotoImage(file="BitTwister.gif")
w_logo = tk.Label(root, image=logo).pack(side="right")

button_enable = tk.Button(root,text='Enable Motor', width=25, command=enable_motor)
button_enable.pack()

button_stop_motor = tk.Button(root,text='Stop Motor', width=25, command=stop_motor)
button_stop_motor.pack()

button_colckwise = tk.Button(root,text='Rotate Clockwise', width=25, command=rotate_clockwise)
button_colckwise.pack()

button_counter_clockwise = tk.Button(root,text='Rotate Counter-clockwise', width=25, command=rotate_counter_clockwise)
button_counter_clockwise.pack()

button_close = tk.Button(root,text='close', width=25, command=close_all)
button_close.pack()

root.mainloop()

