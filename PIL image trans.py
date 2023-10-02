#!/usr/bin/env python3
import os
from PIL import Image
os.chdir(os.getcwd()+ "/supplier-data/images/")
for image in os.listdir():
#Validate if it's an image in the format we want to change
  if ".tiff" in image:
    #Taking first part of the  name
    name = str(image).split(".")[0]
    with Image.open(image) as im:
      im.convert("RGB").resize((600,400)).save(name + ".jpeg")


