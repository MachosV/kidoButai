import smtplib
from email.mime.text import MIMEText

sender_email = 'useronboard@machosv.me'
sender_password = ''
recipient_email = 'razgriz9@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent using machosv.me as an SMTP relay.'

message = MIMEText(body)
message['Subject'] = "Welcome to QRExp.pro!"
message['From'] = "QRExp.pro"+" "+sender_email
message['To'] = recipient_email

with smtplib.SMTP_SSL('mail.machosv.me', 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())