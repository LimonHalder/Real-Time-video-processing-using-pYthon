import cv2
import mediapipe as mp
import time



class poseDetector():
    def __init__(self, static_image_mode=False,model_complexity=1,smooth_landmarks=True,enable_segmentation=False,smooth_segmentation=True,min_detection_confidence=0.5,min_tracking_confidence=0.5):

        self.static_image_mode=static_image_mode
        self.model_complexity=model_complexity
        self.smooth_landmarks=smooth_landmarks
        self.enable_segmentation=enable_segmentation
        self.smooth_segmentation=smooth_segmentation
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose()
        self.mpdraw=mp.solutions.drawing_utils


    def findPose(self,img, draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpdraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)


        return img

    def findPosition(self,img , drae=True):
        list=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                cx,cy= int(lm.x*h),int(lm.y*w)
                #print(id,lm)
                list.append([id,cx,cy])
                if id == 0:
                    cv2.circle(img, (cx, cy), 12, (255, 0, 255), cv2.FILLED)

        return list




def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detectior=poseDetector()
    while True:
        succes, img = cap.read()
        img=detectior.findPose(img)
        list=detectior.findPosition(img)
        print(list)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS:{int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)
        cv2.imshow("Img",img)
        cv2.waitKey(1)


if __name__ == '__main__':
        main()