# utils.py

def get_priority(text: str):
    text = text.lower()

    if "urgent" in text:
        return "High"
    elif "important" in text:
        return "Medium"
    else:
        return "Low"


# ================= EMAIL FUNCTION (SendGrid) =================

import os
import requests
from dotenv import load_dotenv

# Load env variables (local ke liye)
load_dotenv()


def send_email(receiver_email, otp):
    print("Sending email via SendGrid...")

    api_key = os.getenv("SENDGRID_API_KEY")
    sender_email = os.getenv("EMAIL")

    # 🔥 Safety check
    if not api_key or not sender_email:
        raise Exception("❌ SENDGRID_API_KEY or EMAIL missing")

    url = "https://api.sendgrid.com/v3/mail/send"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "personalizations": [
            {
                "to": [{"email": receiver_email}],
                "subject": "Password Reset OTP - Smart Task API"
            }
        ],
        "from": {"email": sender_email},
        "content": [
            {
                "type": "text/plain",
                "value": f"""
Hi,

Your OTP is: {otp}

This OTP is valid for 5 minutes.

Do not share it with anyone.

- Smart Task API
"""
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 202:
            print("✅ Email sent successfully via SendGrid")
        else:
            print("❌ Error:", response.text)

    except Exception as e:
        print("❌ Exception:", e)
