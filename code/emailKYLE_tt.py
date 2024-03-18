import smtplib
from email.mime.text import MIMEText
import datetime

def sendlogTOkyle():
    log = open("./ZZ_logs/gen.log", "r")
    now = datetime.datetime.now()

    sender = 'contact@kyle-seaford.co.uk'
    receivers = ['projects@kyle-seaford.co.uk']
    smtp_server = 'smtp.ionos.co.uk' 
    smtp_port = 587
    smtp_username = '' 
    smtp_password = '' 

    # Build the message with MIMEText for proper formatting
    message = MIMEText(f"See the attached log file for autoTT from {now}\n\n{log.read()}")
    message['Subject'] = f"autoTT log {now}"
    message['From'] = sender
    message['To'] = ', '.join(receivers)

    try:
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.starttls()  
        
        smtpObj.login(smtp_username, smtp_password)
        
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
    finally:
        log.close()
