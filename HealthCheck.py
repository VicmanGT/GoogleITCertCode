#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails
import os
import time

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free /du.total * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 80

def check_memory_usage():
  usage = psutil.virtual_memory()[3]
  return usage/1000000 < 500

def check_localhost():
  try:
    return socket.gethostbyname("localhost") == "127.0.0.1"
  except:
    return False

def main():
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "Please check your system and resolve the issue as soon as possible."
  if check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, receiver,subject,body)
    emails.send_email(message)
  elif check_disk_usage("/"):
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)
  elif check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)
  elif check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

starttime = time.time()
while True:
  if __name__ == "__main__":
    main()
    print("tick")
    time.sleep(60 - ((time.time())-starttime)%60)
