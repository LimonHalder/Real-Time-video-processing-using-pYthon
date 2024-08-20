import cv2
import time
import mediapipe as mp
from mediapipe.python._framework_bindings import packet

class handdetection():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon,
                                        self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils


    def findhands(self,img, draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handLms, self.mpHands.HAND_CONNECTIONS)
        return img



    def findPosition(self,img, draw=True,handNo=0):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myhand =self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myhand.landmark):

                 h, w, c = img.shape
                 cx, cy = int(lm.x * w), int(lm.y * h)
                 lmList.append([id,cx,cy])

                 if draw:   #if id == 0:
                    cv2.circle(img,(cx,cy),12, (255,0,255),cv2.FILLED)
        return lmList
def main():

    pTime = 0
    cap = cv2.VideoCapture(0)
    detector=handdetection()
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

if __name__ == '__main__':
    main()