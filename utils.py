def get_priority(text: str):
    text = text.lower()

    if "urgent" in text:
        return "High"
    elif "important" in text:
        return "Medium"
    else:
        return "Low"
    
    
import os
import smtplib
from email.mime.text import MIMEText


def send_email(receiver_email, otp):
    print("Connecting to Gmail...")
    
    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    subject = "Your OTP Code"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()    
    print("Email sent successfully")
