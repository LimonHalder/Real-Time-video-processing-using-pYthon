import time

import cv2

from HandTrakingModule as htm


pTime = 0
cap = cv2.VideoCapture(0)
detector=htm.
while True:
    success, img = cap.read()
    img=detector.findhands(img)
    lmList=detector.findPosition(img)

    if len(lmList) !=0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)