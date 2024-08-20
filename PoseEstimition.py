import cv2
import mediapipe as mp
import time


mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpdraw=mp.solutions.drawing_utils
cTime=0
pTime=0
cap=cv2.VideoCapture(0)
while True:
    succes, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)

    if results.pose_landmarks:
        mpdraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy= int(lm.x*h),int(lm.y*w)
            print(id,lm)
            if id == 0:
                cv2.circle(img, (cx, cy), 12, (255, 0, 255), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)
    cv2.imshow("Img",img)
    cv2.waitKey(1)