#!/usr/bin/env python3
import os
import os.path
import datetime
import emails
import reports
def main():
  descriptions = []
  attachment_path = "/tmp/processed.pdf"
  os.chdir(os.getcwd()+ "/supplier-data/descriptions/")
  for description in os.listdir():
    with open(description) as opened:
      fruit = "<br/>name: " + opened.readline() + "<br/>"
      fruit += "weight: " + opened.readline() + "<br/>"
      fruit = fruit.replace("\n","")
      descriptions += [fruit]
      print(descriptions)
  descriptions = str(descriptions).strip("[]").replace("'","").replace(",","")
  title = "Processed Update on " + str(datetime.datetime.today())
  reports.generate_report(attachment_path, descriptions, title)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender,receiver,subject,body,attachment = attachment_path)
  emails.send_email(sender,message)
if __name__ == "__main__":
  main()

