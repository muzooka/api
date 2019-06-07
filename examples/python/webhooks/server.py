import os
import atexit
import json
import requests
import hashlib
import hmac
from flask import Flask, request

MUZOOKA_API_KEY = os.environ.get('MUZOOKA_API_KEY')
MUZOOKA_API_URL = 'https://devapi-qc.muzooka.com/v2'
NGROK_URL = os.environ.get('NGROK_URL')
MUZOOKA_AUTH_HEADERS = {
    'x-api-key': MUZOOKA_API_KEY,
}

app = Flask(__name__)
my_webhooks = []

if not MUZOOKA_API_KEY:
    print('MUZOOKA_API_KEY is missing')
if not NGROK_URL:
    print('NGROK_URL is missing')


# Creates an HMAC SHA1 signature using a key and payload
def make_signature(key, payload):
    key = bytes(key, 'UTF-8')
    digester = hmac.new(key, payload, hashlib.sha1)
    signature = digester.hexdigest()
    return 'sha1={}'.format(signature)


# On application exit all existing webhooks are deleted
def on_app_exit():
    for webhook in my_webhooks:
        print('deleting webhook: {}'.format(webhook['id']))
        requests.delete(
            '{}/webhooks/{}'.format(MUZOOKA_API_URL, webhook['id']),
            headers=MUZOOKA_AUTH_HEADERS
        )


atexit.register(on_app_exit)

# Use this route to create a new webhook, expects a muzookaId to exist in the
# request body, and for the body to be in JSON format. Returns the webhook id
# and the Muzooka id of the created webhook.
@app.route('/webhooks', methods=['POST'])
def create_webhook():
    content = request.json
    muzooka_id = content['muzookaId']

    webhook_payload = {
        'type': 'page',
        'filter': muzooka_id,
        'url': '{}/webhooks-listen'.format(NGROK_URL),
    }
    webhook_response = requests.post(
        '{}/webhooks'.format(MUZOOKA_API_URL),
        json=webhook_payload,
        headers=MUZOOKA_AUTH_HEADERS,
    )

    webhook = {
        'id': webhook_response.json()['id'],
        'muzooka_id': muzooka_id,
    }

    my_webhooks.append(webhook)
    return json.dumps(webhook)


# This route listens for updates from Muzooka, when an update is received the
# signature of the request body is calculated and compared to the signature
# provided by Muzooka
@app.route('/webhooks-listen', methods=['POST'])
def webhooks_listen():
    raw_content = request.get_data()
    artist = request.json
    signature = request.headers.get('X-Signature')
    calculated_signature = make_signature(MUZOOKA_API_KEY, raw_content)

    name = artist['name'] if (artist and 'name' in artist) else 'undefined'
    print('Webhook received for artist: {}'.format(name))
    print('Webhook signature: {}'.format(signature))
    print('Calculated signature: {}'.format(calculated_signature))

    print(artist)

    if signature == calculated_signature:
        print('Signatures match, content came from Muzooka')
        # This is where you would update your local store for the given artist
    else:
        print('Signatures do not match, content did not come from Muzooka')
        # Do not update you local store with the data provided, this request
        # may not have come from Muzooka

    return 'ok'
