import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
SMS_KEY = os.getenv("SMS_KEY")
NUMBER = os.getenv("NUMBER")
RECEIVER_NUMBER = os.getenv("RECEIVER_NUMBER")

client = Client(ACCOUNT_SID, SMS_KEY)


def send_message(text):
    message = client.messages.create(
        body=text,
        from_=NUMBER,
        to=''
    )
