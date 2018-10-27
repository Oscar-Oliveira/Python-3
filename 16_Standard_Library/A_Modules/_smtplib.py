"""
smtplib
"""

import smtplib

EMAIL_HOST = "smtp.mailtrap.io"
EMAIL_HOST_USER = "1ccd1fc0462e08"
EMAIL_HOST_PASSWORD = "f2d750abd80bd4"
EMAIL_PORT = "2525"

from_email = "oscar.m.oliveira@gmail.com"

to = ["oscar.m.oliveira@gmail.com", "oscar.m.oliveira@outlook.com"]

subject = "Some subject..."
text = "Some text..."

body = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}".format(from_email, ", ".join(to), subject, text)

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
server.sendmail(from_email, to, body)
server.quit()

print("Done!")
