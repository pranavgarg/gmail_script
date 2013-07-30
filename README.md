gmail_script
============

Python Script to send automated emails from your gmail account based on certain dates/times.
Configuration option to be set in the sendMail function of send_email.py
<pre>
 gmailUser = GMAIL USER ACCOUNT
 gmailPassword = GMAIL PASSWORD/APPLICATION SPECIFIC PASSWORD
</pre>
Please refer to <a href="https://support.google.com/mail/answer/1173270?hl=en">this site</a> to generate application specific password using your gmail account. 
<pre>
recipient = RECIPIENT EMAIL
</pre>


Once you have provided the above configuration. Run the script by typing <b> python send_email.py </b> to see if it works fine. 
If there is an error it will report it out on the terminal.

Schedule it for later running by using crontab -e to schedule the job to run every week or daily etc. 
for e.g. 
<pre>
0 17 * * 0,3 python   PATH_TO_THE_FILE_send_email.py
</pre>
