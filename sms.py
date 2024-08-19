from twilio.rest import Client
import auth_token,account_sid

with open(auth_token, 'r') as file:
    auth_token = file.read().strip()
with open(auth_sid, 'r') as file:
    auth_sid = file.read().strip()
client = Client(account_sid, auth_token)

def sendsms():
    message = client.messages.create(
    from_='+12565764479',
    body='Alert',
    to='+18777804236'
    )
    print(message.sid)