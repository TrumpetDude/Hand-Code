from __future__ import division
import time
import Adafruit_ADS1x15
import Adafruit_PCA9685

adc = Adafruit_ADS1x15.ADS1115()
pwm = Adafruit_PCA9685.PCA9685()

GAIN = 1
channel = 0

pwm.set_pwm_freq(60)
inputValues = [5000,5000,5000,5000,5000]

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    inputValues.insert(0, adc.read_adc(channel, gain=GAIN))
    inputValues.pop()
    #servoValue = int(sorted(inputValues)[2]/62+355) #servo
    servoValue = int(sorted(inputValues)[2]/50+275) #linear actuator
    '''if servoValue<420:
	    servoValue = 420
    if servoValue>780:
	    servoValue = 780'''
    print (servoValue)
    print (inputValues[2])
    pwm.set_pwm(0, 0, int(servoValue))#thumb
    pwm.set_pwm(1, 0, int(servoValue))#index
    pwm.set_pwm(2, 0, int(servoValue))#middle
    pwm.set_pwm(3, 0, int(servoValue))#ring
    pwm.set_pwm(4, 0, int(servoValue))#pinky

