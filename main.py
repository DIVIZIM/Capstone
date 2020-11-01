# import the necessary packages 
from imutils.video import FPS
import numpy as np 
import time 
import math 
import cv2 as cv 
import wiringpi
from enum import Enum
from ina219 import INA219
from ina219 import DeviceRangeError

#GLOBAL SETTINGS
DEBUG = 1
HIGH = 1
LOW = 0
OUTPUT = 1
INPUT = 0

#SETUP CAMERA SETTINGS
capture0_width = 320
capture0_height = 320
capture1_width = 320
capture1_height = 320

#create 2 VideoCapture object 
capture0 = cv.VideoCapture(0)
capture0.set(3,capture0_width)
capture0.set(4,capture0_height)
capture1 = cv.VideoCapture(2)
capture1.set(3,capture1_width)
capture1.set(4,capture1_height)

#check they are open
if DEBUG:
    if (capture0.isOpened() == False): 
        print('Error while trying to open camera0. Plese check again...') 
    if (capture1.isOpened() == False): 
        print('Error while trying to open camera1. Plese check again...')
    
ret0, frame0 = capture0.read()
ret1, frame1 = capture1.read()

#INCU Setup
net = cv.dnn.readNet('facedetection/face-detection-adas-0001.bin', 'facedetection/face-detection-adas-0001.xml')
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)

#DEMULTIPLEXER SETUP
T_DELAY = .001
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

def decimalToBinary(n):
    return bin(n).replace("0b", "").zfill(3)

def initilizeWiringPi():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(OutputY.A.value, OUTPUT)
    wiringpi.pinMode(OutputY.B.value, OUTPUT)
    wiringpi.pinMode(OutputY.C.value, OUTPUT)
    wiringpi.pinMode(OutputX.S0.value, OUTPUT)
    wiringpi.pinMode(OutputX.S1.value, OUTPUT)
    wiringpi.pinMode(OutputX.S2.value, OUTPUT)
    wiringpi.pinMode(G, OUTPUT)
    wiringpi.pinMode(D, OUTPUT)
    
    wiringpi.digitalWrite(OutputY.A.value, LOW)
    wiringpi.digitalWrite(OutputY.B.value, LOW)
    wiringpi.digitalWrite(OutputY.C.value, LOW)
    wiringpi.digitalWrite(OutputX.S0.value, LOW)
    wiringpi.digitalWrite(OutputX.S1.value, LOW)
    wiringpi.digitalWrite(OutputX.S2.value, LOW)
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
    (y,x) = element
    x = decimalToBinary(x)
    y = decimalToBinary(y)
    
    i = 0
    for z in OutputX:
        if(int(x[i]) == 0):
            wiringpi.digitalWrite(int(z.value),LOW)

        else:
            wiringpi.digitalWrite(int(z.value),HIGH)

        i += 1
    
    i = 0
    for z in OutputY:
        if(int(y[i]) == 0):
            wiringpi.digitalWrite(int(z.value),LOW)

        else:
            wiringpi.digitalWrite(int(z.value),HIGH)

        i +=1
        
    #Pulse the output to turn on/off a selected aray element
    wiringpi.digitalWrite(G,HIGH)
    wiringpi.digitalWrite(D,value)
    time.sleep(T_DELAY)
    wiringpi.digitalWrite(G,LOW)
    time.sleep(T_DELAY)

def updateArray(update,history):
    threshold = 5
    maximum = 10
    for x in range(0,8):
        for y in range(0,8):
            if(update[y][x] > history[y][x][0]):
                if(history[y][x][1] >= threshold):
                    setElement((y,x),update[y][x])
                    history[y][x][0] = update[y][x]
                else:
                    if(history[y][x][1] <= maximum):
                        history[y][x][1]+= 1 
            elif(update[y][x] == history[y][x][0]):
                if(update[y][x]):
                    if(history[y][x][1] <= maximum):
                        history[y][x][1]+= 1 
                else:
                    if(history[y][x][1] >= -maximum):
                        history[y][x][1]-= 1 
            else:
                if(history[y][x][1] <= -threshold):
                    setElement((y,x),update[y][x])
                    history[y][x][0] = update[y][x]
                else:
                    if(history[y][x][1] >= -maximum):
                        history[y][x][1]-= 1 
            
#CURRENT SENSOR SEUP
"""
SHUNT_OHMS = 0.1
AMP = 2.0
ina = INA219(SHUNT_OHMS,AMP)
ina.configure(ina.RANGE_16V)
"""
array_elements = [ [[0 for k in range(2)] for i in range(8) ] for j in range(8) ]
# capture frames from the camera 
while(capture0.isOpened() and capture1.isOpened()):   
    
    """
    #SOFTWARE CURRENT PROTECTION
    if(ina.current() > CURRENT_MAX):
        for x in range(0,8):
            for y in range(0,8):
                setElement((x,y),0)
        break
    """
    face_pos_x,face_pos_y,sun_pos_x,sun_pos_y = 0,0,0,0
    if DEBUG:
        print("------------------------")
        print("array_elements")
        for i in array_elements:
            print(i)
        print("------------------------")
                
    ret0, frame0 = capture0.read()
    ret1, frame1 = capture1.read()     
    
    if ret1 == True:
        blob = cv.dnn.blobFromImage(frame1, size=(160, 120))
        net.setInput(blob)
        out = net.forward()
        for detection in out.reshape(-1, 7):
            confidence = float(detection[2])
            if confidence > 0.7:
                xmin = int(detection[3] * frame1.shape[1])
                ymin = int(detection[4] * frame1.shape[0])
                xmax = int(detection[5] * frame1.shape[1])
                ymax = int(detection[6] * frame1.shape[0])
                face_pos_x = ((xmax + xmin)/2)/(capture1_width/8)
                face_pos_y = (2/3*(ymax-ymin)+ymin)/(capture1_height/8)

        if ret0 == True: 
            blur = cv.GaussianBlur(frame0, (5, 5), 2)                
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)  
             
             
            ret,thresh = cv.threshold(gray,230,255,cv.THRESH_BINARY) 
            thresh = cv.dilate(thresh, None, iterations=1) 
            #thresh = cv.erode(thresh,None,iterations=1) 
             
            contours,hierarchy = cv.findContours(thresh, 1, 2) 
             

            if len(contours) > 0:
                temp = [ [ 0 for i in range(8) ] for j in range(8) ]
                #Sort Contors by area 
                for cnts in contours:                    
                    if(cv.contourArea(cnts)>10): 
                        (x,y),radius = cv.minEnclosingCircle(cnts) 
                        if DEBUG:
                            center = (int(x),int(y)) 
                            radius = int(radius) 
                            frame0 = cv.circle(frame0,center,radius+5,(255,0,0),2)
                            
                        #print(int((x-radius)/capture0_width*8))
                        #temp[int(x/capture0_width*8)][int(y/capture0_width*8)] = 1
                            
                        for ax in range(int((x-radius)/capture0_width*8),int((x+radius)/capture0_width*8)):
                            for ay in range(int((y-radius)/capture0_height*8),int((y+radius)/capture0_height*8)):
                                if(ax >= 0 and ay >= 0 and ax <=7 and ay<=7):
                                    temp[ay][ax] = 1
                                                                              
                updateArray(temp,array_elements)
                                
                        
                                 
            #else: 
                #if DEBUG: 
                    #print('Sorry No contour Found ' , time.ctime()) 
        else: 
            break
             
    # show the frame 
    if DEBUG: 
        cv.imshow("Frame0", frame0)
        cv.imshow("Frame1", frame1) 
    key = cv.waitKey(1) & 0xFF 
    # if the `q` key was pressed, break from the loop 
    if key == ord("q"): 
        break 

     
#cleanup 
cv.destroyAllWindows()
capture0.release()
capture1.release() 
