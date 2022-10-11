# python3 adv/network/email_test.py

import smtplib

sender = 'bategoy738@kaimdr.com'
receivers = ['sk***@hotmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail(sender, receivers, message)         
  print("Successfully sent email")
except Exception:
  print("Error: unable to send email")