import smtplib
from app.config import config


class SendMail:
    def __init__(self, name, email, message):
        self.name = name,
        self.email = email,
        self.message = message

    def send_mail(self, name, email, message):
        # SET THE INFO ABOUT THE SAID EMAIL
        sent_from = email
        sent_to = config['gmail_user']
        sent_subject = "Request Info"
        sent_body = (""" 
        %s\n\n
        %s 
        """) % (message, name)

        email_text = """
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (sent_from, sent_to, sent_subject, sent_body)

        # SEND EMAIL OR CRASH TRYING!!!
        try:
            mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            mail.ehlo()
            mail.login(sent_to, config['gmail_app_password'])
            mail.sendmail(sent_from, sent_to, email_text)
            mail.close()

            return 'Email sent!'
        except Exception as exception:
            return "Error: %s!\n\n" % exception
