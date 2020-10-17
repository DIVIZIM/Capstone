import wiringpi
import time
from enum import Enum

class OutputY(Enum):
    O1 = 5
    O2 = 6
    O3 = 13
    
class OutputX(Enum):
    O1 = 17
    O2 = 27
    O3 = 22
    
SET = 12
OUTPUT = 16

HIGH = 1
LOW = 0

def decimalToBinary(n):
    return int(bin(n).replace("0b", ""))

def initilize():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(OutputY.O1.value, HIGH)
    wiringpi.pinMode(OutputY.O2.value, HIGH)
    wiringpi.pinMode(OutputY.O3.value, HIGH)
    wiringpi.pinMode(OutputX.O1.value, HIGH)
    wiringpi.pinMode(OutputX.O2.value, HIGH)
    wiringpi.pinMode(OutputX.O3.value, HIGH)
    wiringpi.pinMode(SET, HIGH)
    wiringpi.pinMode(OUTPUT, HIGH)
    
    wiringpi.digitalWrite(OutputY.O1.value, LOW)
    wiringpi.digitalWrite(OutputY.O2.value, LOW)
    wiringpi.digitalWrite(OutputY.O3.value, LOW)
    wiringpi.digitalWrite(OutputX.O1.value, LOW)
    wiringpi.digitalWrite(OutputX.O2.value, LOW)
    wiringpi.digitalWrite(OutputX.O3.value, LOW)
    wiringpi.digitalWrite(SET, LOW)
    wiringpi.digitalWrite(OUTPUT, LOW)

#2D vector for location of array
# 012
#0
#1
#2
def setElement(element,value):
    (x,y) = element
    x = decimalToBinary(x)
    y = decimalToBinary(y)
    
    for z in OutputX:
        if(x%10 == 0):
            wiringpi.digitalWrite(z.value,0)
            print(x)
        else:
            wiringpi.digitalWrite(z.value,1)
            print(x)
        x = int(x/10)
        
    for z in OutputY:
        if(y%10 == 0):
            wiringpi.digitalWrite(z.value,0)
        else:
            wiringpi.digitalWrite(z.value,1)
        y = int(y/10)
        
    #Pulse the output to turn on/off a selected aray element
    wiringpi.digitalWrite(OUTPUT,value)
    wiringpi.digitalWrite(SET, 1)
    time.sleep(.01) #wait 10 ms for signal to propogate
    wiringpi.digitalWrite(SET, 0)
    
initilize()
setElement((3,2),1)

while True:
    print("Hello")
    break;