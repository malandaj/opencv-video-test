import cv2

def changeBrightness(x):
    brightness = cv2.getTrackbarPos('brightness','image')
    brightness = (brightness - 0)/(255 - 0)
    print(brightness)
    cap.set(10,brightness)

def changeContrast(x):
    contrast = cv2.getTrackbarPos('contrast','image')
    contrast = (contrast - 0)/(255 - 0)
    print(contrast)
    cap.set(11,contrast)
    
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
#get current brightness and contrast values
bright = int(round(cap.get(10) * 255));
contra = int(round(cap.get(11) * 255));
cv2.createTrackbar('brightness','image',bright,255,changeBrightness)
cv2.createTrackbar('contrast','image',contra,255,changeContrast)

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