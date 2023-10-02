#!/usr/bin/env python3
import requests
import os
url="http://localhost/upload/"
os.chdir(os.getcwd()+ "/supplier-data/images/")
for image in os.listdir():
  if ".jpeg" in image:
    with open(image, "rb") as opened:
      r = requests.post(url, files={"file":opened})
      print(r.ok)