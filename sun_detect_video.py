# import the necessary packages
from imutils.video import FPS
import numpy as np
import imutils
import time
import math
import cv2 as cv

def checkSun(frame,center,radius):
    test = [160,195,170]
    counter = 0
    sampleArea = 5
    for rad in range(0,12):
        x,y = center
        x = x + int(radius*math.cos(rad * math.pi / 6))
        y = y + int(radius*math.sin(rad * math.pi / 6))
        temp = averageColor(frame,x,y,sampleArea)
        if(test[0] > temp[0] and test[1] < temp[1] and test[2] < temp[2]):
            counter += 1
    return counter

def averageColor(frame,x,y,area):
    average = [0, 0, 0]
    counter = 0
    for ax in range(x-area,x+area):
        for ay in range(y-area,y+area):            
            if((ax > (frame_width -1)) or (ax < 0) or (ay > (frame_height -1)) or (ay < 0)):
                counter += 1
            else:
                average = [sum(i) for i in zip(average,frame[ay,ax])]                
    div = (4*area*area - counter)
    if (div != 0):
        average[:] = [int(x / div) for x in average]
        return average
    else:
        return [0,0,0]

fps = FPS().start()

for counter in range(0,10):
    file = '/home/pi/opencv/capstone/videos/' + str(counter) + '.MOV'
    output = '/home/pi/opencv/capstone/output/' + 'outpi - ' + str(counter) + '.avi'

    # create VideoCapture object
    capture = cv.VideoCapture(file)
    if (capture.isOpened() == False):
        print('Error while trying to open ' + file + '. Plese check again...')

    # get the frame width and height and modifyqqq
    frame_width = int(capture.get(3)/5)
    frame_height = int(capture.get(4)/5)
    out = cv.VideoWriter(output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    # capture frames from the camera
    while(capture.isOpened()):
    #grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
        ret, frame = capture.read()
        if ret == True:
        
            frame = cv.resize(frame,(frame_width,frame_height),fx=0,fy=0,interpolation = cv.INTER_CUBIC)
            blur = cv.GaussianBlur(frame, (5, 5), 2)               
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY) 
            
            
            ret,thresh = cv.threshold(gray,227,255,cv.THRESH_BINARY)
            #thresh = cv.dilate(thresh, None, iterations=3)
            #thresh = cv.erode(thresh,None,iterations=1)
            
            contours,hierarchy = cv.findContours(thresh, 1, 2)
            

            if len(contours) > 0:
                #Sort Contors by area
                for cnts in contours:

                    epsilon = 0.1*cv.arcLength(cnts, True)
                    approx = cv.approxPolyDP(cnts, epsilon, True)
                    (x,y),radius = cv.minEnclosingCircle(cnts)
                    center = (int(x),int(y))
                    radius = int(radius)
                    if(checkSun(frame,center,radius) > 0):
                        frame = cv.circle(frame,center,radius,(0,255,0),2)
                    else:
                        print('no contour that contains sun pixles ' , time.ctime());
            else:
                print('Sorry No contour Found ' , time.ctime())
        else:
            break
        
        # show the frame
        cv.imshow("Frame", frame)
        fps.update()
        circles = 0
        out.write(frame)
        key = cv.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv.destroyAllWindows()
