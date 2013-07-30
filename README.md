gmail_script
============

Script to send automatic emails from your gmail based on certain dates written in Python.
Details to be set in the sendMail function. 

 gmailUser = '<GMAIL USER ACCOUNT>'
 gmailPassword = "<GMAIL PASSWORD/APPLICATION SPECIFIC PASSWORD>"
                Please refer to this site. https://support.google.com/mail/answer/1173270?hl=en
 recipient = '<email to which the email should be sent to>' 


Once you have provided the above configuration. Run the script by typing python <b>send_email.py</b> to see if it works fine. 
If there is an error it will report it out on the terminal.

Schedule it for later running by using crontab -e to schedule the job to run every week or daily etc. 
for e.g. 
0 17 * * 0,3 python /<PATH TO THE FILE>/edlab_runner.py
