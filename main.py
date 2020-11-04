import numpy as np
import cv2
import PIL
import PIL.Image

cap = cv2.VideoCapture(0)
CAPTURE = r"resources\large_image.png"
BALL = r"resources\small_image.png"

def find(large_image, small_image, method = cv2.TM_SQDIFF_NORMED):
    small_image = cv2.imread(BALL)
    large_image = cv2.imread(CAPTURE)
    result = cv2.matchTemplate(small_image, large_image, method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    trows,tcols = small_image.shape[:2]

    return [MPx, MPy, MPx+tcols, MPy+trows]

font = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    ret, frame = cap.read()
    cv2.imwrite(CAPTURE, frame)
    coords = find(CAPTURE, BALL)
    x = coords[0]
    y = coords[1]

    cv2.rectangle(frame, (x,y),(coords[2],coords[3]),(0,0,255),2)
    cv2.putText(frame, f"x: {x}, y: {y}",(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('Tennis Ball Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()