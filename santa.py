import smtplib
from email.mime.text import MIMEText
from random import randint

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
    was generated from a Python script written by Jeremy P-K. You can see the code yourself <a 
    href="https://github.com/Timshel-JPK/SecretSanta2025">here</a>! 
   </small></small></p> </body> </html>"""


def send_email():
    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())
    print("Email sent to", recipient_email, "!")


taken = []
santa_dict = {}
santa_dict[1] = 'alec@1'
santa_dict[2] = 'cote@1'
santa_dict[3] = 'dom@1'


# santa_dict[4] = 'ian@1'
# santa_dict[5] = 'james@1'
# santa_dict[6] = 'jeremy@1'
# santa_dict[7] = 'kabeer@1'
# santa_dict[8] = 'kamal@1'
# santa_dict[9] = 'liam@1'
# santa_dict[10] = 'steven@1'

# 10 people. Person N gets their number added to the 'self' list, so they can't receive themselves.
# Person N then gets a random number 1-10, and that person (Person Y) is who they will gift to.
# Person Y then gets their number added to the 'taken' list, so they can not be selected again.
# Remove Person N from the 'self' list
# Move on to Person N + 1, repeat all above steps
def randomize_santas(i):
    self = [i]
    y = (randint(1, len(santa_dict)))
    #print(y)
    while (y in self) | (y in taken):
        y = (randint(1, len(santa_dict)))
        #(y)

    taken.append(y)
    print(santa_dict[i], " giving to ", santa_dict[y])


i = 1
while len(santa_dict) != len(taken):
    #if len(taken) == len(santa_dict) -1:
    randomize_santas(i)
    i += 1
#send_email()
