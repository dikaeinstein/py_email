import smtplib
import ssl
import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL

sender_email = input('Enter sender email address and press enter: ')
receiver_email = input('Enter receiver email address and press enter: ')
password = getpass.getpass("Enter email password and press enter: ")

message = MIMEMultipart('alternative')
message['Subject'] = 'Multipart test'
message['From'] = sender_email
message['TO'] = receiver_email

# Create HTML and plain text message
html = '''\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
'''

text = '''\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(receiver_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
