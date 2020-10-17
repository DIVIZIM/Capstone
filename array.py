import wiringpi
import time
from enum import Enum

class OutputY(Enum):
    A = 5
    B = 6
    C = 13
    
class OutputX(Enum):
    A = 17
    B = 27
    C = 22
    
G = 12
D = 16

HIGH = 1
LOW = 0

def decimalToBinary(n):
    return bin(n).replace("0b", "").zfill(3)

def initilize():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(OutputY.A.value, HIGH)
    wiringpi.pinMode(OutputY.B.value, HIGH)
    wiringpi.pinMode(OutputY.C.value, HIGH)
    wiringpi.pinMode(OutputX.A.value, HIGH)
    wiringpi.pinMode(OutputX.B.value, HIGH)
    wiringpi.pinMode(OutputX.C.value, HIGH)
    wiringpi.pinMode(G, HIGH)
    wiringpi.pinMode(D, HIGH)
    
    wiringpi.digitalWrite(OutputY.A.value, LOW)
    wiringpi.digitalWrite(OutputY.B.value, LOW)
    wiringpi.digitalWrite(OutputY.C.value, LOW)
    wiringpi.digitalWrite(OutputX.A.value, LOW)
    wiringpi.digitalWrite(OutputX.B.value, LOW)
    wiringpi.digitalWrite(OutputX.C.value, LOW)
    wiringpi.digitalWrite(G, HIGH)
    wiringpi.digitalWrite(D, LOW)

#2D vector for location of array
# 01
#0
#1
#
#(ABC,ABC)
#(000,000)
def setElement(element,value):
    (x,y) = element
    x = decimalToBinary(x)
    y = decimalToBinary(y)
    
    i = 0
    for z in OutputX:
        if(x[i] == 0):
            wiringpi.digitalWrite(z.value,0)
        else:
            wiringpi.digitalWrite(z.value,1)
        i += 1
        
    i = 0
    for z in OutputY:
        if(y[i] == 0):
            wiringpi.digitalWrite(z.value,0)
        else:
            wiringpi.digitalWrite(z.value,1)
        i += 1
        
    #Pulse the output to turn on/off a selected aray element
    wiringpi.digitalWrite(D,value)
    wiringpi.digitalWrite(G, LOW)
    time.sleep(.01) #wait 10 ms for signal to propogate
    wiringpi.digitalWrite(G, HIGH)
    
initilize()
setElement((3,2),1)

while True:
    print("Hello")
    break;