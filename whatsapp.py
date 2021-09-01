import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

client = Client()

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919711026442'

client.messages.create(body = 'Ahoy World!', 
						from_=from_whatsapp_number, 
						to=to_whatsapp_number)