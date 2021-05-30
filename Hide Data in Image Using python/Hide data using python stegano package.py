# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:52:54 2021

@author: Dhiraj Wagh
"""
from stegano import lsb

#choose an image with path
images = "/images/dhiraj.png"


#Select the name of the new image that contains the data.
new_img = "python_dhiraj.png"

#Choose the text of  the message that you want to hide in the new image.
msg = "Hi, I am Dhiraj, this is my personal text."

# to hide message.
lsb.hide(images, message = msg).save(new_img)

# to reveal hidden message.
message = lsb.reveal(new_img)

#check the secreat text.
print("Hidden message : ", message)
