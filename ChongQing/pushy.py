import json
import urllib.request


class PushyAPI:
    @staticmethod
    def sendPushNotification(data, ids):
        # Insert your Pushy Secret API Key here
        apiKey = 'a9b3279a3070b877c296db7971b2a629019bfe3725435eb2d6f5f86f49453ab1'

        # Set post variables
        postData = {
            'data': data,
            'registration_ids': ids
        }

        # Set URL to Send Notifications API endpoint
        req = urllib.request.Request('https://api.pushy.me/push?api_key=' + apiKey)

        # Set Content-Type header since we're sending JSON
        req.add_header('Content-Type', 'application/json')

        print(json.dumps(postData))

        # Actually send the push
        response = urllib.request.urlopen(req, json.dumps(postData).encode('utf-8'))
