# -*- coding: utf-8 -*-
"""
Created on Sun May 30 08:48:56 2021

@author: Dhiraj Wagh
"""


# importing packages. 
import pyautogui
import cv2
import numpy as np

# resolution specification

resolution = pyautogui.size()

# specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of output file
filename = "Recording.avi"

#specify frames rate. wa can chhose
# any value and experiment with it.
fps = 60.0

# Creating a VideoWriter Object
out = cv2.VideoWriter(filename, codec,
                      fps, resolution)


#Creating windows to show live recording

# creating an empty window.
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resize this windows
cv2.resizeWindow("Live", 480, 270)


# Infinite loop for record screen
while True:
    img = pyautogui.screenshot()   # Take screenshot using pyautogui
    
    frame = np.array(img)# convert screenshot to numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    out.write(frame)  # Write it to the output file.
    cv2.imshow("Live", frame)   
    
    
    
    # stop recording when we press q
    if cv2.waitKey(1) == ord('q'):
        break
    
    
# release resources and destory
out.release()   # release the video writer

# Destory all windows.
cv2.destroyAllWindows()