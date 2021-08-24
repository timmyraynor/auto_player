import mss
import cv2
import numpy as np
import sys
import imagehash

print('操作系统:', sys.platform)
scalar=False

upleft = (0, 0)
if scalar==True:
    downright = (568,374)
else:
    downright = (1200, 700)
a,b = upleft
c,d = downright
monitor = {"top": b, "left": a, "width": c, "height": d}

with mss.mss() as mss_instance:  # Create a new mss.mss instance
    monitor_1 = mss_instance.monitors[1]  # Identify the display to capture
    screenshot = mss_instance.grab(monitor_1)  # Take the screenshot
    im = np.array(screenshot)
    screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    cv2.imshow('test.png',screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
