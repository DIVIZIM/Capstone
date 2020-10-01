# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv



for counter in range(0,10):
    file = '/home/pi/opencv/capstone/videos/' + str(counter) + '.MOV'
    output = '/home/pi/opencv/capstone/output/outpy' + str(counter) + '.avi'
    # create VideoCapture object
    capture = cv.VideoCapture(file)
    if (capture.isOpened() == False):
        print('Error while trying to open ' + file + '. Plese check again...')
    # get the frame width and height
    frame_width = int(capture.get(3)/4)
    frame_height = int(capture.get(4)/4)
    out = cv.VideoWriter(output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    # capture frames from the camera
    while(capture.isOpened()):
    #grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
        ret, frame = capture.read()
        if ret == True:
            frame = cv.resize(frame,(frame_width,frame_height),fx=0,fy=0,interpolation = cv.INTER_CUBIC)
            blur = cv.GaussianBlur(frame, (5, 5), 2)   
            #blur = cv.medianBlur(img,5)    
            gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
            
            ret,thresh = cv.threshold(gray,237,255,cv.THRESH_BINARY)
            #thresh = cv.erode(thresh,None,iterations=2)
            #thresh = cv.dilate(thresh, None, iterations=2)

            contours,hierarchy = cv.findContours(thresh, 1, 2)
            
            
            if len(contours) > 0:
                #Sort Contors by area
                for cnts in contours:
                    if cv.contourArea(cnts) > 0:
                        epsilon = 0.1*cv.arcLength(cnts, True)
                        approx = cv.approxPolyDP(cnts, epsilon, True)
                        (x,y),radius = cv.minEnclosingCircle(cnts)
                        center = (int(x),int(y))
                        radius = int(radius)
                        frame = cv.circle(frame,center,radius,(0,255,0),2)
                    else:
                        print('Sorry No contour Found Large Enough.')
            else:
                print('Sorry No contour Found.')
        else:
            break
        
        # show the frame
        cv.imshow("Frame", frame)
        out.write(frame)
        key = cv.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
