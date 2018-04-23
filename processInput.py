from __future__ import division
import time
import Adafruit_ADS1x15#Analog to digital for Myoware
import Adafruit_PCA9685#Servos and Linear Actuators
#import libraries for program flow and hardware

#initialize Analog to Digital Converter and Pulse Width Modulation objects
adc = Adafruit_ADS1x15.ADS1115()
pwm = Adafruit_PCA9685.PCA9685()

GAIN = 1 #Set the gain. This needs to be experimented with to find the most reliable results.

pwm.set_pwm_freq(60)#frequency good for servos
inputValues = [5000,5000,5000,5000,5000]#initialize the list at of the last 5 inputs at low values

#note: Apart from the equations used to set their positions, servos and linear actuators are interchangeable.

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:#execution loop
    inputValues.insert(0, adc.read_adc(channel, gain=GAIN))#add the most recent input to the front of the list
    inputValues.pop()#remove the least recent input from the end of the list
    #equations calculated at https://www.desmos.com/calculator/6ftevgrchz
    #servoValue = int(sorted(inputValues)[2]/62+355) #convert ADC input to servo output
    servoValue = int(sorted(inputValues)[2]/50+275) #same as above, but for linear actuator
    '''if servoValue<420:
	    servoValue = 420
    if servoValue>780:
	    servoValue = 780'''#limits on movement
    print (servoValue)#display value servo has been set to
    print (inputValues[2])#display median of 5 most recent input values (used to calculate where the servo is set)
    pwm.set_pwm(0, 0, int(servoValue))#thumb
    pwm.set_pwm(1, 0, int(servoValue))#index
    pwm.set_pwm(2, 0, int(servoValue))#middle
    pwm.set_pwm(3, 0, int(servoValue))#ring
    pwm.set_pwm(4, 0, int(servoValue))#pinky

