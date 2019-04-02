import sys
import time
import RPi.GPIO as GPIO
import PCA9685 as p 



pwm = p.PWM(bus_number=1)
pwm.frequency = 60

choix = 0
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


def reverse(x):
    GPIO.output(Motor0_A, GPIO.LOW)
    GPIO.output(Motor0_B, GPIO.HIGH)
    GPIO.output(Motor1_A, GPIO.LOW)
    GPIO.output(Motor1_B, GPIO.HIGH) 
    time.sleep(x)
    

def forward(x):
    GPIO.output(Motor0_A, GPIO.HIGH)
    GPIO.output(Motor0_B, GPIO.LOW)
    GPIO.output(Motor1_A, GPIO.HIGH)
    GPIO.output(Motor1_B, GPIO.LOW)  
    time.sleep(x)

def stop():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)    

        
#setSpeed(204)

try :
    
        

        while(True):
            choix = input("choisissez la vitesse : 1 - 2 - 3 - 4. 5=stop")
            if(choix == 1):
                forward(3)
                setSpeed(51)
                
            elif(choix == 2):
                forward(3)
                setSpeed(102)
                
            elif(choix == 3):
                forward(3)
                setSpeed(153)
                
            elif(choix == 4):
                forward(3)
                setSpeed(204)

	    elif(choix == 5):
		stop()
    
except KeyboardInterrupt :
    print("Keyboard interrupt")
finally:
    print("clean up") 
    stop()
    GPIO.cleanup()
    

