import cv2
from cvzone.PoseModule import PoseDetector
import sms
detector = PoseDetector()


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

l=[]
while True:
    success,img = cap.read()
    img = detector.findPose(img)
    imlist,bbpx=detector.findPosition(img)
    

    if len(imlist) > 0:
        print("Human Detected")
        l.append(1)
    if len(l) > 5  and flag:
        flag = False
        sms.sendSms()
    cv2.imshow("output", img)
    q = cv2.waitkey(1)
    if q ==ord('q'):
        break
