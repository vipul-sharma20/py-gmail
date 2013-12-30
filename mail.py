def send_email():
    import smtplib

    gmail_user = "sender@gmail.com"
    gmail_pwd = "password-of sender@gmail.com"
    FROM = 'sender@gmail.com'
    TO = ['receiver@gmail.com'] #must be a list
    SUBJECT = "Testing sending using gmail"
    TEXT = "Testing sending mail using gmail servers"
    # Prepare actual message
    try:
	      message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
      	server.ehlo()
        server.starttls()
      	server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
send_email()
