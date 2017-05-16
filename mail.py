import smtplib


def send_email():
    gmail_user = "sender@gmail.com"
    gmail_pwd = "password-of sender@gmail.com"
    FROM = 'sender@gmail.com'
    TO = ['receiver@gmail.com']  # must be a list
    SUBJECT = "Testing sending using gmail"
    TEXT = "Testing sending mail using gmail servers"

    try:
        # Prepare actual message
        message = """\From: {from_}\nTo: {to}\nSubject: {subject}\n\n{text}
        """.format(from_=FROM,
                   to=", ".join(TO),
                   subject=SUBJECT,
                   text=TEXT)

        # or port 465 doesn't seem to work!
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # greeting to receiver smtp, verifies the sender's SMTP
        server.ehlo()

        # Transfer Layer Security, enables encryption
        server.starttls()

        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")


if __name__ == '__main__':
    send_email()
