import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

'''
  sendMail function sends email from a gmail account using the gmail account details
  to the account or listserv to which you want to send.
  Input Params: Subject - Subject of the email
                Text - text of the email
                HTML - html of the email (is mainly used for displaying on readers which can render HTML emails) 
'''
def sendMail(subject, text, html):
  gmailUser = '<GMAIL USER ACCOUNT>'
  gmailPassword = '<GMAIL PASSWORD/APPLICATION SPECIFIC PASSWORD'
  recipient = '<EMAIL TO SENT TO'
  msg = MIMEMultipart('alternative')
  msg['From'] = gmailUser
  msg['To'] = recipient
  msg['Subject'] = subject
  
  msg.attach(MIMEText(text,'plain'))
  msg.attach(MIMEText(html,'html'))


  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmailUser, gmailPassword)
  print msg.as_string()
  mailServer.sendmail(gmailUser, recipient, msg.as_string())
  mailServer.close()
  print('Sent email to %s' % recipient)



sendMail('EdLab Runner\'s Club',"""
Hi Everybody,

Get ready for tomorrow's run at 5:15PM. Don't forget to bring your running gear.
Looking forward to see you all.

- EdLab Running Club
""","""<html>
<head></head>
<body>
<p>Hi Everybody!<br>
   <p>
   A gentle reminder about tomorrow's EdLab run at 5:30PM.<br>
   Please <b>don't forget to bring your running gear</b>.
   </p> <br>
   <br>
   - EdLab Runners Club
  </body></html>""")
