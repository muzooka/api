Python Webhooks Example Server
==============================

In this example Flask and [ngrok](https://ngrok.com/) are used to create a simple server that can
create and listen to Webhooks from Muzooka's API. In this example server HMAC authentication has
been implemented so you can verify that the webhook came from Muzooka.

This example was written in Python 3, it may work with Python 2, but it has not been tested.


## Setting Up
- Create an account for [ngrok](https://ngrok.com/) and install the binary on your system
- Either clone this repository, or copy `server.py` and `requirements.txt` to your local machine
- Install the requirements using `pip install -r requirements.txt`, we suggest you use
  [Virtualenv](https://virtualenv.pypa.io/) to isolate your environment
- In one terminal, start ngrok: `./ngrok http 5000`
- Note the `Forwarding` http address (it will look something like `https://xxx.ngrok.io`
- In another terminal, start the flask server:
  `FLASK_APP=server.py MUZOOKA_API_KEY=xxx NGROK_URL=https://xxx.ngrok.io flask run`


## Testing
- Create a new webhook by POSTing to `localhost:5000/webhooks` with a JSON body similar to the
  following, replacing `{{muzookId}}` with the page you want to follow (should be a page that you can
  make changes to):
  ```json
  {
    "muzookaId": "{{muzookaId}}",
  }
  ```
- Example cURL statement:
```bash
curl -X POST \
  http://localhost:5000/webhooks \
  -H 'Content-Type: application/json' \
  -H 'content-length: 34' \
  -d '{"muzookaId": "foofighters"}'
```
- Make a change to the page in Muzooka and wait for the change to propagate (15 minutes)
- You should see in your console a statement like so:
```
Webhook received for artist: Some Artist
Webhook signature: sha1=d4f8a60ac0c30dcf76a4052ec61e4b1aa7637603
Calculated signature: sha1=d4f8a60ac0c30dcf76a4052ec61e4b1aa7637603
Signatures match, content came from Muzooka
```
- Upon closing the server, any webhooks you created will be automatically deleted
