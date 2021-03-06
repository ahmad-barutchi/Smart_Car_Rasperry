rom __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

def tourner():
    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()

    # Configure min and max servo pulse lengths
    servo = 475  # Min pulse length out of 4096

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(channel, 0, pulse)

    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
        # Move servo on channel O between extremes.
        pwm.set_pwm(0, 0, servo)
        time.sleep(0.5)
        servo-=20
        print(servo)
        if servo <= 300:
            servo = 600
        # 475 tout droit

    # Reinitialisation des parametres GPIOs
        GPIO.cleanup()

tourner()