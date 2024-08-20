import time
import cv2
import HandTrakingModule as htm
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

pTime = 0
cap = cv2.VideoCapture(0)
detection=htm.handdetection(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volumRange=volume.GetVolumeRange()

minvol=volumRange[0]
maxvol=volumRange[1]
vol=0
volBar=400
while True:
    success, img = cap.read()
    img=detection.findhands(img)
    lmList=detection.findPosition(img, draw=False)

    if len(lmList)!=0:


        x1,y1= lmList[4][1],lmList[4][2]
        x2,y2=lmList[8][1],lmList[8][2]
        cx,cy= (x1+x2)//2,(y1+y2)//2


        cv2.circle(img, (x1,y1), 12,(255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 12, (255, 0, 255), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2), (255,0,255),3)
        cv2.circle(img ,(cx,cy), 10, (255,0,255), cv2.FILLED)

        length=math.hypot(x1-x2,y1-y2)
        vol = np.interp(length, [50, 180], [minvol, maxvol])
        volBar = np.interp(length, [50, 180], [400,150])
        volume.SetMasterVolumeLevel(vol, None)
        print(vol)
        if length<=50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)


    #volume.SetMasterVolumeLevel(0.0, None)

    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)