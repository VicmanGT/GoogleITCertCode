
#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass
def generate_email(sender, receiver, subject, body, attachment=None):
  message = EmailMessage()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = subject
  message.set_content(body)
  if attachment:
    attachment_filename = os.path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment, "rb") as ap:
      message.add_attachment(ap.read(),
                             maintype = mime_type,
                             subtype=mime_subtype,
                             filename=attachment_filename)
  return message
def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  print(mail_server)
  mail_server.send_message(message)
  mail_server.quit()

