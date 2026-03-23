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

    # 🔥 ADD THIS (IMPORTANT)
    print("DEBUG EMAIL:", sender_email)
    print("DEBUG PASSWORD:", app_password)

    if not sender_email or not app_password:
        raise Exception("❌ EMAIL or APP_PASSWORD not found in environment variables")

    subject = " Password Reset OTP - Smart Task API"

    #  FIX: body function ke andar hona chahiye
    body = f"""
Hi,

You recently requested to reset your password.

Your OTP (One-Time Password) is:
👉 {otp}

⏳ This OTP will expire in 5 minutes.

⚠️ For security reasons, do not share this OTP with anyone.

If you did not initiate this request, you can safely ignore this email.

Thanks & Regards,  
Smart Task API Team  
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Error:", e)
