# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC3a6a3aa1d7e96bcfd822a588df067ebe'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+919791694834',
							body ='body',
							to ='+919940340451'
						)

print(message.sid)
