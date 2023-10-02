#! /usr/bin/env python3
import os
import requests
import re

os.chdir("/data/feedback")
for file in os.listdir("/data/feedback"):
    with open(file) as review:
        contents = {"title":"", "name": "", "date": "", "feedback": ""}
        #Extract the lines and strip new line characters
        title = review.readline()
        contents["title"] = title.strip()
        name = review.readline()
        contents["name"] = name.strip()
        date = review.readline()
        contents["date"] = date.strip()
        feedback = review.readlines()
        #Make the last part a str, then filter the []
        str_feedback = str(feedback)
        clean_feedback = re.search(r"[\w\.,!' ]+", str_feedback)
        contents["feedback"]= clean_feedback[0]
    print(contents)
    #The last "/" in the URL it's important
    response = requests.post("http://34.170.242.5/feedback/", json=contents)
    if response.ok:
        print("Succesful POST for {}".format(file))
    else:
        raise Exception("POST failes with status code {} for {}".format(response.status_code, file))

