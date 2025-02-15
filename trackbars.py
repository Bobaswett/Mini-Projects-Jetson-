import cv2

dispW=320
dispH=240



def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cv2.namedWindow('LogiCam')
cv2.createTrackbar('x','LogiCam',0, 320, nothing)
cv2.createTrackbar('y','LogiCam',0,240,nothing)
cv2.createTrackbar('size', 'LogiCam',5,100,nothing)

while True: 
    ret, frame=cam.read()
    
    xval = cv2.getTrackbarPos('x','LogiCam')
    yval = cv2.getTrackbarPos('y','LogiCam')
    size = cv2.getTrackbarPos('size','LogiCam')
    
    cv2.circle(frame,(xval, yval),size,(255,0,0),-1)
   
    cv2.imshow('LogiCam', frame)   
    cv2.moveWindow('LogiCam', 0, 0)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()