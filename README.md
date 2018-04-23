# Hand Code

## High-Level Description of Code Function and Hardware Used

The script "processInput.py" takes input from a [MyoWare Muscle Sensor](https://www.adafruit.com/product/2699) through an [Analog to Digital Converter](https://www.adafruit.com/product/1085) (ADC) and sets [servos](https://www.sparkfun.com/products/9065) or [linear actuator](https://www.actuonix.com/PQ12-Micro-Linear-Actuators-s/1825.htm) according to the input recieved. The code runs on a Raspberry Pi (we are using a Pi 2).

## Nitty-Gritty Code Stuff

### Overview of Program Flow

The program runs in an infinite loop after importing the necessary libraries and initializing variables and objects for the devices. The 5 most recent values are stored in a list, and each time the loop iterates and a value is taken, it is added to the list and the least recent input value is removed. The list is ordered least to greatest and the median value is used to set the position of the servo or linear actuator. 

### Libraries
`from __future__ import division`
Let the interpreter know to look for more modules.

`import time`
Not currently used in the program. This is used for debugging if we want to run code with preprogrammed input.

`import Adafruit_ADS1x15`
Library for the ADC

`import Adafruit_PCA9685`
Library for Servo Hat

A list of libraries that had to be installed on the pi before use can be found [here](https://docs.google.com/document/d/1wVpSVv_SawRpC-WruQutOTwtWMYNuBGmzVt4C7Bn6ZA/edit?usp=sharing).

### Conversion from MyoWare input values to Servo and Linear Actuator output values

Input values from the Myoware sensor's EMG electrodes, after going through the ADC, range from roughly 4000 (relaxed) to 26000 (tensed). We can experiment with the gain on the sensor and in the code to adjust this, although we have not done so yet. Two equations are used to convert this rnage of values into a corresponding range for servos (**need to find range and adjust equation**) and linear actuators (**need to find range and adjust equation**).
