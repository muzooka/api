# Muzooka API

## How To Request An API Key

1. Login to [Muzooka](https://app.muzooka.com/m/login).
2. Verify your Facebook account and permissions, then you will be directed to the Profile Manager.
3. Click on your avatar and then [API Keys](https://app.muzooka.com/m/developers).
4. Click the blue `Request API Key` button.
5. Once approved you will receive an email from Muzooka. [Login](https://app.muzooka.com/m/login) and return to the [Developer](https://app.muzooka.com/m/developers) section.
6. To attain your key, click on `Click to reveal key`.

## API Usage & Terms of Service

Using the Muzooka API indicates that you accept and will comply with the [Muzooka Terms of Service](https://www.muzooka.com/legal) (see section 12 for API Usage Terms). 

Your API key must be sent in an http header called `X-api-key` for all requests to the API.

To ensure that you always have the most up-to-date artist assets, we strongly recommend integrating the Muzooka API using webhooks. That way, you cache artist assets on your system until you receive a webhook notification from our system letting you know a profile was updated on Muzooka.

Read more in our [webhook integration guide](webhooks.md).

If you integrate the Muzooka API without using webhooks, you are required to check our system every 24 hours for updates to ensure that the artist assets on your system are always current.

<sub>\* For questions, please contact us at api@muzooka.com.</sub>

## Restful API
For the most current version of our API please view the [v2 documentation](v2.md)
