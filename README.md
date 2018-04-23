# Hand-Code

## High-Level Description of Code Function

The script "processInput.py" takes input from a MyoWare muscle sensor through an Analog to Digital Converter (ADC) and sets servos or linear actuators according to the input recieved. The code runs on a Raspberry Pi (we are using a Pi 2).

## Nitty-Gritty Code Stuff

### Overview of Program Flow

The program runs in an infinite loop after importing the necessary libraries and initializing variables and objects for the devices. The 5 most recent values are stored in a list, and each time the loop iterates and a value is taken, it is added to the list and the least recent input value is removed. The list is ordered least to greatest and the median value is used to set the position of the servo or linear actuator. 
