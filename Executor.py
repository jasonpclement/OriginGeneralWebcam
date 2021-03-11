import threading
import time
import OriginCameraInterface

myScannedBarCode = 'BootID1234'
myCameraName = 'AssemblyLine6'
myTargetDir = r"C:\Users\jason\OneDrive\Documents\repos\OriginGeneralWebcam\outputFiles"
myTargetFileName = f"{myScannedBarCode}_{myCameraName}.mp4"


#instantiate an OriginCamera Object
originCamera = OriginCameraInterface.OriginCamera()


#simulate a barcode scan
print(f"worker just scanned barcode {myScannedBarCode}")
[print('...') for x in range(3)]

#Assign the scanned barcode to the object
originCamera.AssignBarCode(myScannedBarCode)

#commence video thead
thread_StartVideo = threading.Thread(target=originCamera.StartVideo, args=(myTargetDir, myTargetFileName))
thread_StartVideo.start()

#simulate some time where worker is working
for i in range(10):
    time.sleep(2)
    if i%3 == 0:
        print("worker continues to work")
    else:
        print("...")

#Worker presses a stop button
originCamera.StopVideo()

#wait for thread to finish up
thread_StartVideo.join()


print("video complete")