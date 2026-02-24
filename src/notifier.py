# format email body with event details
# connnect securely to SMTP
# send email to user with new events
# handle SMTP errors
# log success/failure of email sending

import smtplib
from email.message import EmailMessage
from src.config import Config

def send_email(events):
    msg = EmailMessage()
    msg['Subject'] = "New Concerts Announced!! :P"
    msg['From'] = Config.EMAIL_ADDRESS
    msg['To'] = Config.EMAIL_ADDRESS

    body = "New concerts that have been announced:\n\n"

    for events in events:
        body += (
            f"Event: {events['event_name']}\n"
            f"Date: {events['event_date']}\n"
            f"Venue: {events['venue']}\n"
            f"City: {events['city']}\n"
            f"URL: {events['url']}\n\n"
        )

    msg.set_content(body)

    with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
        server.starttls()
        server.login(Config.EMAIL_ADDRESS, Config.EMAIL_PASSWORD)
        server.send_message(msg)