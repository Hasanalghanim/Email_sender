import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


# Opens and reads email List as text

email_list = open("email_list.txt", mode="r")
email_list = email_list.readlines()


# Inputs documents, from, subject and message
email = EmailMessage()
email["from"] = "YOUR NAME"
email["to"] = email_list
email["subject"] = "THE SUBJECT"
email.set_content("""\
Hello,

this is where you would put the EMAIL msg Content as a para.

thank you,
:)
""")


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("alghanimhasan2@gmail.com", "Nadiasimmer1")
    smtp.send_message(email)
    print("all good")


# THIS PROJECT WILL NOT WORK IF YOU HAVE *Less secure app access* from your email turned OFF.
