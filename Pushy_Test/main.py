# Import Pushy API class
from pushy import PushyAPI

# Payload data you want to send to devices
data = {'message': '999'}

# The recipient device registration IDs
registration_ids = ['6ed6292be4ac96e7b68e9e']

# Send the push notification with Pushy
PushyAPI.sendPushNotification(data, registration_ids)
