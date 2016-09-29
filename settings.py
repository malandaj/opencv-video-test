import cv2

def changeBrillo(x):
    brillo = cv2.getTrackbarPos('brillo','image')
    brillo = (brillo - 0)/(255 - 0)
    cap.set(10,brillo)

def changeContraste(x):
    brillo = cv2.getTrackbarPos('contraste','image')
    brillo = (brillo - 0)/(255 - 0)
    cap.set(10,brillo)
    
cv2.namedWindow('image')
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
print("FRAME_WIDTH", cap.get(3))
print("FRAME_HEIGHT", cap.get(4))
cap.set(5,30.0)
print("FPS", cap.get(5))
print("BRIGHTNESS", cap.get(10))
print("CONTRAST", cap.get(11))
print("SATURATION", cap.get(12))
print("GAIN", cap.get(14))
print("FOCUS", cap.get(28))
# create trackbars for color change
cv2.createTrackbar('brillo','image',0,255,changeBrillo)
cv2.createTrackbar('contraste','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('image',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()