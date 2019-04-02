import sys
import time
import RPi.GPIO as GPIO
import PCA9685 as p 



pwm = p.PWM(bus_number=1)
pwm.frequency = 60


Motor0_A=11
Motor0_B=12
Motor1_A=13
Motor1_B=15
pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]
EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5
GPIO.setmode(GPIO.BOARD) 
for pin in pins:
		GPIO.setup(pin, GPIO.OUT)



def setSpeed(speed):
	speed *= 20	
	pwm.write(EN_M0, 0, speed)
	pwm.write(EN_M1, 0, speed)


def forward(x):
    GPIO.output(Motor0_A, GPIO.LOW)
    GPIO.output(Motor0_B, GPIO.HIGH)
    GPIO.output(Motor1_A, GPIO.LOW)
    GPIO.output(Motor1_B, GPIO.HIGH) 
    time.sleep(x)
    

def reverse(x):
    GPIO.output(Motor0_A, GPIO.HIGH)
    GPIO.output(Motor0_B, GPIO.LOW)
    GPIO.output(Motor1_A, GPIO.HIGH)
    GPIO.output(Motor1_B, GPIO.LOW)  
    time.sleep(x)

def stop():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)    

        
setSpeed(204)

try :
    while (1):
        forward(5)
        reverse(5)
    
except KeyboardInterrupt :
    print("Keyboard interrupt")
finally:
    print("clean up") 
    stop()
    GPIO.cleanup()
    

