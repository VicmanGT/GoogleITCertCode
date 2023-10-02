#! /usr/bin/env python3
import os
import requests
url = "http://localhost/fruits/"
content = {"name":" ", "weight": 0, "description": " ", "image_name": " "}
os.chdir(os.getcwd()+ "/supplier-data/descriptions/")
for description in os.listdir():
  with open (description) as file:
    content["name"] = file.readline().strip("\n")
    content["weight"] = int(file.readline().strip(" lbs\n"))
    content["description"] = str(file.readlines()).strip("[]").replace("'","").replace("\\n","").replace("\\xa0","").strip(" ,")
    content["image_name"] =  str(description).replace(".txt",".jpeg")
    r = requests.post(url, data = content)
    print(r.ok)