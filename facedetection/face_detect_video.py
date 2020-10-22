import cv2 as cv

net = cv.dnn.readNet('face-detection-adas-0001.bin', 'face-detection-adas-0001.xml')
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)

file = 'face.mp4'

capture = cv.VideoCapture(file)

while(capture.isOpened()):
    ret, frame = capture.read()
    if not ret:
        break
    frame_width = int(capture.get(3)/5)
    frame_height = int(capture.get(4)/5)
    frame = cv.resize(frame,(frame_width,frame_height),fx=0,fy=0,interpolation = cv.INTER_CUBIC)

    blob = cv.dnn.blobFromImage(frame, size=(frame_width, frame_height))
    net.setInput(blob)
    out = net.forward()

    for detection in out.reshape(-1, 7):
        confidence = float(detection[2])
        xmin = int(detection[3] * frame.shape[1])
        ymin = int(detection[4] * frame.shape[0])
        xmax = int(detection[5] * frame.shape[1])
        ymax = int(detection[6] * frame.shape[0])

        if confidence > 0.5:
            cv.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))

    cv.imshow('OpenVINO face detection', frame)
    key = cv.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
            
cv.destroyAllWindows()