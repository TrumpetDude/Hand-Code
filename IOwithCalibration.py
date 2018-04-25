from __future__ import division
import time
import Adafruit_ADS1x15#Analog to digital for Myoware
import Adafruit_PCA9685#Servos and Linear Actuators
#import libraries for program flow and hardware

#initialize Analog to Digital Converter and Pulse Width Modulation objects
adc = Adafruit_ADS1x15.ADS1115()
pwm = Adafruit_PCA9685.PCA9685()

GAIN = 4 #Set the gain. Can vary from user to user
channel = 0 #set the channel for analog input

pwm.set_pwm_freq(60)#frequency good for servos
inputValues = [5000,5000,5000,5000,5000]#initialize the list at of the last 5 inputs at low values

calibrated=False

mode = "linear actuator"
minValue = 260
maxValue = 550
#mode = "servo"
#minValue = 200
#maxValue = 665


'''
while calibrated=False:
    #tell user to relax, get resting value
    #tell user to tense, get maximum values
    #generate equation (scale and shift)
'''

#note: Apart from the equations used to set their positions, servos and linear actuators are interchangeable.

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('Moving servo on channel 0, press Ctrl-C to quit...')

while True:#execution loop

    inputValues.insert(0, adc.read_adc(channel, gain=GAIN))#add the most recent input to the front of the list
    inputValues.pop()#remove the least recent input from the end of the list
    
    outputValue = int(sorted(inputValues)[2]/scale+shift) #convert ADC input to output
    if outputValue<minValue:
	    outputValue = minValue
	if outputValue>maxValue:
	       outputValue = maxValue
	       
	#manual input: 
    #outputValue = int(input("Output Value: "))
	
    print (outputValue)#display value servo has been set to
    print (inputValues[2])#display median of 5 most recent input values (used to calculate where the servo is set)
    
    pwm.set_pwm(0, 0, int(outputValue))#thumb
    pwm.set_pwm(1, 0, int(outputValue))#index
    pwm.set_pwm(2, 0, int(outputValue))#middle
    pwm.set_pwm(3, 0, int(outputValue))#ring
    pwm.set_pwm(4, 0, int(outputValue))#pinky
