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

dc = 100.0 # Dutycycle for PWM (0.00 <= dc <= 100)
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
    global dc, pwm_freq
    
    try:
        dc = float(dc_entry.get()) # Copy user entry to dc variable
    except:
        print('Using dc value {}'.format(dc))
    
    try:
        pwm_freq = float(freq_entry.get()) # Copy user entry to freq variable
    except:
        print('Using freq value {}'.format(pwm_freq))
        
    pwm_signal.ChangeDutyCycle(dc)
    pwm_signal.ChangeFrequency(pwm_freq)
    print('Modifying PWM signal with Duty Cycle & {}% Frequency {}'.format(dc, pwm_freq))

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

    tk.Label(root, text="PWM Duty cycle %").pack()
    dc_entry = tk.Entry(root)
    dc_entry.pack()

    #dc_entry = tk.Scale(root, from_=0, to=100, resolution=1, orient='horizontal')
    #dc_entry.pack()


    freq_entry = tk.Scale(root, from_=0.1, to=9.9, resolution=0.1, digits=2, orient='horizontal')
    freq_entry.pack()
    tk.Label(root, text="PWM Frequency").pack()

    #tk.Label(root, text="PWM Frequency").pack()
    #freq_entry = tk.Entry(root)
    #freq_entry.pack()

    button_pwm = tk.Button(root,text='Modify PWM', width=25, command=modify_pwm)
    button_pwm.pack()

    button_close = tk.Button(root,text='close', width=25, command=close_all)
    button_close.pack()

    root.mainloop()

