# -*- coding: utf-8 -*-
"""
Created on Sun May 30 08:37:24 2021

@author: Dhiraj Wagh
"""

import urllib.request
import cv2
import numpy as np
import time

URL = " "  # put your IP here

while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow("IPwebcam", img)
    
    
    
    if cv2.waitKey(1):
        break
    