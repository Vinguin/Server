#!/usr/bin/python

import sys
import smtplib


# 0 = sendmail.py
# 1 = sender_email
# 2 = receiver_email
sender = "rss@vingu.online"
receivers = ["vinhngu62@yahoo.de", "christopher.bate@web.de"]
text = ""

changelog_file = open("new_titles.txt", "r")
changelog_text = changelog_file.readlines()
changelog_file.close()


# Format Text to be sent
for item in changelog_text:
    text = text+" > "+item

message = """From: RSS-Feed <"""+sender+""">
To: To Person <"""+receivers[0]+""">
Subject: Physical Review Letters

Hey, es gibt neue Paper zu lesen!

"""+text+"""

http://journals.aps.org/prl/

--
RSS Feed for Shelly



"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email" + str(receivers)
except SMTPException:
    print "Error: unable to send email"
