import smtplib
from email.mime.text import MIMEText
from ..config import SENDER_EMAIL
from ..config import SENDER_PASSWORD
from ..config import SMTP_SERVER

def sendMail(recipient_email,subject,body):

    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = "QRExp.pro"
    message['To'] = recipient_email

    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def main():
    print("Running tests")

if __name__=="__main__":
    main()