from __future__ import division
import time
import Adafruit_ADS1x15#Analog to digital for Myoware
import Adafruit_PCA9685#Servos and Linear Actuators
#import libraries for program flow and hardware

#initialize Analog to Digital Converter and Pulse Width Modulation objects
adc = Adafruit_ADS1x15.ADS1115()
pwm = Adafruit_PCA9685.PCA9685()

GAIN = 1 #Set the gain. 
channel = 0 #set the channel for analog input

pwm.set_pwm_freq(60)#frequency good for servos
inputValues = [5000,5000,5000,5000,5000]#initialize the list at of the last 5 inputs at low values

with open('equationValues.txt', 'r') as f:
	lines = f.readlines()
	scaleFactor = float(lines[0])
	offsetAmount = float(lines[1])
	outputMin = int(lines[2])
	outputMax = int(lines[3])
	print(scaleFactor, offsetAmount, outputMin, outputMax)
	
	
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('Moving servo on channel 0, press Ctrl-C to quit...')

while True:#execution loop

    inputValues.insert(0, adc.read_adc(channel, gain=GAIN))#add the most recent input to the front of the list
    inputValues.pop()#remove the least recent input from the end of the list
    
    outputValue = int(sorted(inputValues)[2]/scaleFactor+offsetAmount) #convert ADC input to servo output
    if outputValue<outputMin:
	    outputValue = outputMin
    if outputValue>outputMax:
        outputValue = outputMax
	       
	#manual input: 
    #outputValue = int(input("Output Value: "))
	
    #print (outputValue)#display value servo has been set to
    print (inputValues[2])#display median of 5 most recent input values (used to calculate where the servo is set)
    
    pwm.set_pwm(0, 0, int(outputValue))#thumb
    pwm.set_pwm(1, 0, int(outputValue))#index
    pwm.set_pwm(2, 0, int(outputValue))#middle
    pwm.set_pwm(3, 0, int(outputValue))#ring
    pwm.set_pwm(4, 0, int(outputValue))#pinky
