import numpy as np
import cv2
import pyautogui
import time

ScreenSize = (1920, 1080)
FourCC = cv2.VideoWriter_fourcc(*"XVID")
OutFile = cv2.VideoWriter("ScreenRecord.avi", FourCC, 5.0, (ScreenSize))
FPS = 60
Prev = 0

while True:
    TimeElapsed = time.time() - Prev
    Image = pyautogui.screenshot()

    if TimeElapsed > 1.0 / FPS:
        Prev = time.time()
        Frame = np.array(Image)
        Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
        OutFile.write(Frame)
    cv2.waitKey(100)

cv2.destroyAllWindows()
OutFile.realese()














