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
PWM_0 = 32 # Pulse width Modulation

dc = 100 # Dutycycle for PWM (0.00 <= dc <= 100)
pwm_freq = 0.5 # PWM frequency

# set up GPIO pins
GPIO.setup(A0, GPIO.OUT) # Enable pin for motor
GPIO.setup(D8, GPIO.OUT) # Rotate Counter-clockwise
GPIO.setup(D7, GPIO.OUT) # Rotate Clockwise
GPIO.setup(PWM_0, GPIO.OUT) # Supply PWM signal

pwm_signal = GPIO.PWM(PWM_0, pwm_freq) # PWM_0=pin number in PI

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

def modify_pwm():
    global dc, dc_1
    dc = int(dc_entry.get())
    pwm_signal.ChangeDutyCycle(dc)
    print('Modifying PWM signal with Duty Cycle {}%'.format(dc))



def close_all():
    print('Closing Everything')
    pwm_signal.stop()
    GPIO.cleanup()
    sys.exit()


if __name__ == "__main__":

    pwm_signal.start(dc)

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

    tk.Label(root, text="Duty cycle %").pack()
    dc_entry = tk.Entry(root)
    dc_entry.pack()
    dc_1 = dc_entry.get()


    button_pwm = tk.Button(root,text='Modify PWM', width=25, command=modify_pwm)
    button_pwm.pack()

    button_close = tk.Button(root,text='close', width=25, command=close_all)
    button_close.pack()

    root.mainloop()

