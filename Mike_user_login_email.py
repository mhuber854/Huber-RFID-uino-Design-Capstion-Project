import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText

sender = 'mike@michaelehuber.com'
receiver = 'brainmanmike@gmail.com'

message = "Hello World" 
msg = MIMEText(message)

msg['Subject'] = 'Testmessage'
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