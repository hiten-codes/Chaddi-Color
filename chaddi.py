from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class TwilioClient:
    def __init__(self, sid, auth, whatsapp):
        self.client = Client(sid, auth)
        self.whatsapp = whatsapp

    def send_message(self, reciever, body):
        msg = self.client.messages.create(
            from_= self.whatsapp,
            body=body,
            to= reciever
        )

        return msg.sid

if __name__ == "__main__":
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    sandbox_whatsapp = os.getenv("TWILIO_SANDBOX")
    reciever_whatsapp= os.getenv("RECIEVER_WHATSAPP")

    client = TwilioClient(account_sid, auth_token, sandbox_whatsapp)

    client.send_message(reciever_whatsapp, "Good Morning Baby, Aaj Black color ki chaddi pehni hai 😉")