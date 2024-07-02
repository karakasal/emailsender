import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Sender name"
email["to"] = "example@example.com"
email["subject"] = "Subject of email"

email.set_content(html.substitute(name="Test"))

with smtplib.SMTP(host="smtp.hostname.com", port=000) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("example@example.com/loginname", "password")
    smtp.send_message(email)
