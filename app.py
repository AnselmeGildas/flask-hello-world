# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC784e6326d5053cdd3e4049f7d932092f'
auth_token = '3a56ba2bc5366c3c196393879143674d'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='+12565784749',
         body='/tHello world',
         to='+2250788914994'
     )

print(message.body)