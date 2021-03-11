import numpy as np
import cv2



class OriginCamera():
    def __init__(self):
        self.barCode = None
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.isRecording = False


    def AssignBarCode(self, pBarCode):
        self.barCode = pBarCode
        print(f"BarcodeID {self.barCode} assigned to Camera")

    def StopVideo(self):
        self.isRecording = False
        print(f"Video Stopped")


    def StartVideo(self, pTargetDir, pFileName):
        fullPath = f"{pTargetDir}\\{pFileName}"

        self.isRecording = True
        cap = cv2.VideoCapture(0)
        outputFile = cv2.VideoWriter(fullPath,self.codec, 20.0, (640,480))

        while(cap.isOpened() and self.isRecording == True):
            ret, frame = cap.read()
            if ret==True:
                #frame = cv2.flip(frame,0)

                # write the flipped frame
                outputFile.write(frame)

                #cv2.imshow('frame',frame)
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
            else:
                break
        else:
            # Release everything if job is finished
            cap.release()
            outputFile.release()
            cv2.destroyAllWindows()

      

