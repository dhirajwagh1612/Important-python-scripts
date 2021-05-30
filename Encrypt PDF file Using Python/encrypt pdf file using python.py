# -*- coding: utf-8 -*-
"""
Created on Sun May 30 08:16:52 2021

@author: Dhiraj Wagh
"""

# importing PyPDF2 package
from PyPDF2 import PdfFileReader, PdfFileWriter


# Create PdfFileWriter object
out = PdfFileWriter()

# Open our PDF file with the PdfFileWriter
file = PdfFileReader("F:/Projects/Important Python Scripts/Encrypt PDF file Using Python/AI_in_autonomous_vehicles.pdf")

# Get the number of pages in the original file. 
num = file.numPages    # number of pages in the pdf


# Iterate through every page of the original
# file and add it on our new file. 
for idx in range(num):
    # get the page at index idx
    page = file.getPage(idx)
    
    
    # Add it to the output file
    out.addPage(page)
    
    
 # create variable passsword and store.
# our password is in it.   
password = "pass"


# Encrypt the new file with the entered password.
out.encrypt(password)

# Open a new file "myfile_encrypted.pdf"
with open("myfile_encrypted.pdf", "wb") as f:
    # Write our encrypted PDF to this file
    out.write(f)
    