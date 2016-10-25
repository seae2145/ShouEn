import json
import urllib.request


class PushyAPI:
    @staticmethod
    def sendPushNotification(data, ids):
        # Insert your Pushy Secret API Key here
        # apiKey = '8da98c1c0272d8066a77ad92ac26e460774be54d813572cc0f93d45dc1ebe530'
        apiKey = '51ebce2e3e83177f18bbe1ed3de513268d1f123ee037eacafd187faffb91c54b'

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
        print(json.dumps(postData).encode('utf-8'))

        # Actually send the push
        response = urllib.request.urlopen(req, json.dumps(postData).encode('utf-8'))
        # response = urllib.request.urlopen(req, json.dumps(postData))
