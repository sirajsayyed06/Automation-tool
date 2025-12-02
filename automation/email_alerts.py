import smtplib
from email.mime.text import MIMEText
from automation.utils import log

def send_alert(message):
    log("Sending email alert...")

    sender = "your-email@example.com"
    password = "your-email-password"  # use environment vars in real use
    receiver = "receiver@example.com"

    msg = MIMEText(message)
    msg["Subject"] = "Automation Task Notification"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        log("Email sent successfully.")
    except Exception as e:
        log(f"Email sending failed: {e}")
