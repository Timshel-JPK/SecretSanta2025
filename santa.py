import smtplib
from email.mime.text import MIMEText

rec_name = "JEREMY"
recipient_email = "jdude1000@gmail.com"

sender_email = "jeremy.i.pk@gmail.com"
sender_password = "nkwa fpyy hzqa tive"

subject = "Secret Santa 2025"
body = f"""
<html>
  <body>
    <p>For Secret Santa 2025 you will be giving a gift to <b><i>{rec_name}</i></b>!</p> 
    <p><small><small>This email 
    was generated from a Python script written by Jeremy using the information <a 
    href="https://mailtrap.io/blog/python-send-email-gmail/#Setting-up-Python-smtplib-and-email -libraries">here</a> 
    for the email portion.</small></small></p> </body> </html>"""
html_message = MIMEText(body, 'html')
html_message['Subject'] = subject
html_message['From'] = sender_email
html_message['To'] = recipient_email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, html_message.as_string())
