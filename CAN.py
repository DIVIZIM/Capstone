import can
import time
import os
from threading import Thread
import wiringpi
from enum import Enum

DEBUG = 1
DIM_REQUEST = 0x7E8

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
    
#BEGIN CODE
initilizeWiringPi()

if(DEBUG):
    print('\n\rCAN Rx test')
    print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1) 

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
    
print('Ready')

def rxCAN():
    message = bus.recv()    # Wait until a message is received.
    if message.arbitration_id == DIM_REQUEST:
        for i in range(message.dlc):
            x = decimalToBinary(message.data[i])
            print(x)

        if(DEBUG):
            c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
            x = message.data[0]
            print(x)
            s=''
            for i in range(message.dlc ):
                s +=  '{0:x} '.format(message.data[i])
                
            print(' {}'.format(c+s))
def txCAN(arbitration_id,data):
    msg = can.Message(arbitration_id,data,extended_id=False)
    bus.send(msg)
    
try:
    while True:
        rxCAN()
    
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')    
