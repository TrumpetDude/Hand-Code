from __future__ import division
import time
import Adafruit_ADS1x15#Analog to digital for Myoware
import Adafruit_PCA9685#Servos and Linear Actuators
#import libraries for program flow and hardware

#initialize Analog to Digital Converter object
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1 #Set the gain.
channel = 0 #set the channel for analog input

#note: Apart from the equations used to set their positions, servos and linear actuators are interchangeable.


mode = "linear actuator"

calibIterations = 750

print("Please relax your arm as completely as you can.")
time.sleep(5)
print("Detecting resting muscle activity. Please remain relaxed.")
totalResting = 0
for v in range(0,calibIterations):
    totalResting += adc.read_adc(channel, gain=GAIN)
restingValue = totalResting/calibIterations
print(restingValue)
	
print("Please tense your arm as hard as you can.")
time.sleep(3)
print("Detecting tensed muscle activity. Please remain tensed.")
totalTensed = 0
for v in range(0,calibIterations):
	totalTensed += adc.read_adc(channel, gain=GAIN)
tensedValue = totalTensed/calibIterations
print(tensedValue)
		
if mode == "linear actuator":
	outputMin = 260
	outputMax = 550
	scaleFactor = (tensedValue-restingValue)/(outputMax-outputMin)
	offsetAmount = outputMax-(tensedValue/scaleFactor)#could also be outputMin-(restingValue/scaleFactor) with same result
	print(scaleFactor, offsetAmount)
	with open('equationValues.txt', 'w') as f:
		f.truncate(0)
		f.write(str(scaleFactor)+"\n"+str(offsetAmount)+"\n"+str(outputMin)+"\n"+str(outputMax))

if mode == "servo":
	outputMin = 200
	outputMax = 665
	scaleFactor = (tensedValue-restingValue)/(outputMax-outputMin)
	offsetAmount = outputMax-(tensedValue/scaleFactor)#could also be outputMin-(restingValue/scaleFactor) with same result
	print(scaleFactor, offsetAmount)
	with open('equationValues.txt', 'w') as f:
		f.truncate(0)
		f.write(str(scaleFactor)+"\n"+str(offsetAmount)+"\n"+str(outputMin)+"\n"+str(outputMax))
