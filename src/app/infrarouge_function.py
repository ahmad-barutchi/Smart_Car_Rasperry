
import RPi.GPIO as GPIO
import time
import urllib
import os
 
def infra():
    # Utiliser les BCM GPIO et pas les numeros des pins sur P1
    GPIO.setmode(GPIO.BCM)
    
    # Pin GPIO utilisee
    GPIO_PIR = 23

    # Configurer la pin 7 en entree
    GPIO.setup(GPIO_PIR,GPIO.IN)
    
    if GPIO.input(GPIO_PIR)==0:
        print "1"
    else:
        print "0"

    # Reinitialisation des parametres GPIOs
    GPIO.cleanup()


infra()