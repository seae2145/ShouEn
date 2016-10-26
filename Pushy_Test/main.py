# Import Pushy API class
from Pushy_Test.pushy import PushyAPI
# Payload data you want to send to devices
data = {'message': '999'}

# The recipient device registration IDs
# registration_ids = ['dd2c902254468116b2ea2']
registration_ids = ['418720f46bb10272ec7d0d']
# Send the push notification with Pushy
PushyAPI.sendPushNotification(data, registration_ids)
