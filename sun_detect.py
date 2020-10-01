# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 8
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#grab the raw NumPy array representing the image, then initialize the timestamp
# and occupied/unoccupied text
    img = frame.array
    img = cv.resize(img,(320,240),fx=0,fy=0,interpolation = cv.INTER_CUBIC)
    #blur = cv.GaussianBlur(img, (25, 25), 2)   
    blur = cv.medianBlur(img,5)    
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    
    ret,thresh = cv.threshold(gray,254,255,cv.THRESH_BINARY)
    #thresh = cv.erode(thresh,None,iterations=2)
    #thresh = cv.dilate(thresh, None, iterations=2)

    contours,hierarchy = cv.findContours(thresh, 1, 2)
    
    
    if len(contours) > 0:
        #Sort Contors by area
        cnts = sorted(contours, key = cv.contourArea, reverse = True)
        if cv.contourArea(cnts[0]) > 100:
            epsilon = 0.1*cv.arcLength(cnts[0], True)
            approx = cv.approxPolyDP(cnts[0], epsilon, True)
            (x,y),radius = cv.minEnclosingCircle(cnts[0])
            center = (int(x),int(y))
            radius = int(radius)
            img = cv.circle(img,center,radius,(0,255,0),2)
        else:
            print('Sorry No contour Found Large Enough.')
    else:
        print('Sorry No contour Found.')

    # show the frame
    cv.imshow("Frame", img)
    key = cv.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
    	break
