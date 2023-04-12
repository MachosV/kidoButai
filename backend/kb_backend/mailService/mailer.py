import smtplib
from email.mime.text import MIMEText
from ..config import SENDER_EMAIL
from ..config import SENDER_PASSWORD
from ..config import SMTP_SERVER

import string

FORGOTTEN_PASS = 0
SUBSCRIPTION_ACTIVATED = 1
SUBSCRIPTION_CANCELLED = 2
#SUBSCRIPTION_EXPIRED = 3
SUBSCRIPTION_PAYMENT_FAILED = 4
SUBSCRIPTION_RE_ACTIVATED = 5

def sendMail(recipient_email,subject,id=None):

    if subject == FORGOTTEN_PASS:
        subject = "QRExp - Password reset"
        with open("kb_backend/mailService/mailTemplates/resetPassword.html", 'r') as f:
            template = f.read()
    if subject == SUBSCRIPTION_ACTIVATED:
        subject = "QRExp - Welcome on Board"
        with open("kb_backend/mailService/mailTemplates/subscriptionActivated.html", 'r') as f:
            template = f.read()
    if subject == SUBSCRIPTION_CANCELLED:
        subject = "QRExp - Subscription Cancelled"
        with open("kb_backend/mailService/mailTemplates/subscriptionCanceled.html", 'r') as f:
            template = f.read()
    if subject == SUBSCRIPTION_PAYMENT_FAILED:
        subject = "QRExp - Payment Failed"
        with open("kb_backend/mailService/mailTemplates/subscriptionCanceled.html", 'r') as f:
            template = f.read()
    if subject == SUBSCRIPTION_RE_ACTIVATED:
        subject = "QRExp - Subscription re-activated"
        with open("kb_backend/mailService/mailTemplates/subscriptionReActivated.html", 'r') as f:
            template = f.read()

    if id:
        template = template.substitute(id=str(id))

    message = MIMEText(template,"html")
    message['Subject'] = subject
    message['From'] = "QRExp.pro"
    message['To'] = recipient_email

    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())

def main():
    print("Running tests")

if __name__=="__main__":
    main()