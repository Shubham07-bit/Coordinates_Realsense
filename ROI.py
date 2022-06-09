import cv2
import numpy as np
cap = cv2.VideoCapture(1)
ret,frame =cap.read()
frame = cv2.resize(frame,(640,480))
roi = cv2.selectROI(frame)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    print(roi)
    roi_ = frame[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[3])]
    cv2.imshow("ROI",roi_)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
