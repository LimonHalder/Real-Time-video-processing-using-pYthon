import cv2
import time
import mediapipe as mp


cap =cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
cTime=0
pTime=0

while True:
    success ,img =cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
   #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)

                if id==0:
                    cv2.circle(img,(cx,cy),20, (255,0,255),cv2.FILLED)
            mpdraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS:{int(fps)}',(40,70), cv2.FONT_HERSHEY_PLAIN,1 ,(255,0,0),3)


    cv2.imshow("Img",img)
    cv2.waitKey(1)
