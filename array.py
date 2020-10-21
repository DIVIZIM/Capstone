import wiringpi
import time
from enum import Enum

class OutputY(Enum):
    A = 5
    B = 6
    C = 13
    
class OutputX(Enum):
    S0 = 17
    S1 = 27
    S2 = 22
    
G = 12
D = 16

HIGH = 1
LOW = 0

def decimalToBinary(n):
    return bin(n).replace("0b", "").zfill(3)

def initilizeWiringPi():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(OutputY.A.value, HIGH)
    wiringpi.pinMode(OutputY.B.value, HIGH)
    wiringpi.pinMode(OutputY.C.value, HIGH)
    wiringpi.pinMode(OutputX.S0.value, HIGH)
    wiringpi.pinMode(OutputX.S1.value, HIGH)
    wiringpi.pinMode(OutputX.S2.value, HIGH)
    wiringpi.pinMode(G, HIGH)
    wiringpi.pinMode(D, HIGH)
    
    wiringpi.digitalWrite(OutputY.A.value, LOW)
    wiringpi.digitalWrite(OutputY.B.value, LOW)
    wiringpi.digitalWrite(OutputY.C.value, LOW)
    wiringpi.digitalWrite(OutputX.S0.value, LOW)
    wiringpi.digitalWrite(OutputX.S1.value, LOW)
    wiringpi.digitalWrite(OutputX.S2.value, LOW)
    wiringpi.digitalWrite(G, LOW)
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
        i +=1
        
    #Pulse the output to turn on/off a selected aray element
    wiringpi.digitalWrite(D,value)
    wiringpi.digitalWrite(G, HIGH)
    time.sleep(.1) #wait 10 ms for signal to propogate
    wiringpi.digitalWrite(G, LOW)
    
def setElementEncoded(AX,BX,CX,AY,BY,CY, value):
    
    OutputX.A = AX
    OutputX.B = BX
    OutputX.C = CX
    
    OutputY.A = AY
    OutputY.B = BY
    OutputY.C = CY
        
    #Pulse the output to turn on/off a selected aray element
    wiringpi.digitalWrite(D,value)
    wiringpi.digitalWrite(G, LOW)
    time.sleep(.1) #wait 10 ms for signal to propogate
    wiringpi.digitalWrite(G, HIGH)
    
initilize()
time.sleep(.1) #wait 100 ms for signal to propogate

setElement((7,7),0)


while True:
    print("Hello")
    break;