import smtplib
from email.mime.text import MIMEText
from random import randint

sender_email = "jeremy.i.pk@gmail.com"
# This is the old password.. sorry
sender_password = "nkwa fpyy hzqa tive"

email_dict = {'ALEC': 'alecnicholas@hotmail.com',
              'COTE': 'alexcliffordcote@gmail.com',
              'DOM': 'poiriedo@gmail.com',
              'IAN': 'ianmcguire1996@gmail.com',
              'JAMES': 'Jamesgerardbrooks@gmail.com',
              'JEREMY': 'jeremy.i.pk@gmail.com',
              'KABEER': 'Kabeergarba@hotmail.com',
              'KAMAL': 'mirani.kamal@gmail.com',
              'LIAM': 'Liam.cat@hotmail.com',
              'STEVEN': 'Stever12344@msn.com'}
santa_results = {}

subject = "Secret Santa 2025"


def send_email(santa):
    recipient_email = email_dict[santa]

    body = f"""
    <html>
      <body>
        <p>Dear <b>{santa}</b>,</p>
        <p>For Secret Santa 2025 you will be giving a gift to <b><i>{santa_results[santa]}</i></b>!</p> 
        <p>The rules for Secret Santa 2025 are as follows:
        <ol>
          <li>You must get your person something you make with a new skill you learn in 2025</li>
          <li>You must get your person something starting with the letter
          <b>{santa_results[santa][0]}</b></li>
          <li>You have a budget of $150</li>
        </ol>
        </p>
        <p>Have fun, see you guys on New Years Eve!</p>
        <p><small><small>This email 
        was generated from a Python script written by Jeremy P-K. You can see the code yourself <a 
        href="https://github.com/Timshel-JPK/SecretSanta2025">here</a>! 
       </small></small></p> </body> </html>"""

    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())


def randomize_santas():
    santa_results.clear()
    santas = list(email_dict.keys())
    hat = santas[:]

    i = 0
    temp_hold = []

    # Go until the hat is empty and everyone has been assigned someone else
    while len(hat) > 0:
        if list(email_dict.keys())[i] in hat:

            # Take the gifter out of the hat (if they have yet to be picked), so they can't get themselves
            temp_hold.append(santas[i])
            hat.remove(santas[i])

            # Scenario where the last gifter was also the last person who has not been picked
            # When that happens start the randomization process over again
            if len(hat) == 0:
                print("Let's try again!")
                randomize_santas()
                break

        # Pick a random person from the hat to gift to
        y = (randint(0, len(hat) - 1))
        santa_results[santas[i]] = hat[y]

        # Remove the person who got picked from the hat, no getting picked more than once!
        hat.pop(y)

        # Put the gifter back into the hat (if they have not already been picked)
        if len(temp_hold) > 0:
            hat.append(temp_hold[0])
            temp_hold.pop(0)

        i += 1


randomize_santas()
for santa in santa_results:
    send_email(santa)
