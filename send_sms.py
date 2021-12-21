# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('TWILIOACCOUNTSID')
auth_token = os.environ.get('TWILIOAUTH')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14176076477',
                     to='+2348164836050'
                 )

print(message.sid)
