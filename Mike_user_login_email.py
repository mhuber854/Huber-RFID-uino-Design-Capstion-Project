import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText

sender = '*****@gmail.com'
receiver = '******@gmail.com'

message = "USER MIKE RFID Logon" 
msg = MIMEText(message)

msg['Subject'] = 'Someone logged onto USER MIKE on your laptop using RFID'
msg['From'] = sender
msg['To'] = receiver
msg["Date"] = formatdate(localtime=True)

try:
    s = smtplib.SMTP('smtpout.secureserver.net')
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()      
    print ("Successfully sent email")
except smtplib.SMTPException:
    print ("Error: unable to send email")