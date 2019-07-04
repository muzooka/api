# Muzooka API

## How To Request An API Key

1. Login to [Muzooka](https://app.muzooka.com/m/login).
2. Verify your Facebook account and permissions, you will be directed to the Page Manager.
3. On the left navigation, hover over your avatar and click [API Keys](https://app.muzooka.com/m/developers).
4. In the top right, click the blue `Request API Key` button.
5. Once approved you will receive an email from Muzooka, [login](https://app.muzooka.com/m/login) and return to the [Developer](https://app.muzooka.com/m/developers) section.
6. To attain your key, click on `Click to reveal key`.

## API Usage & Terms of Service

The key must be sent in an http header called `X-api-key` for all requests to the API.

In order to use the API, you need to accept and comply with [Muzooka Terms of Service](https://app.muzooka.com/m/legal). Making requests to the API is considered as an act of accepting these terms:

- You agree to cache the JSON response for no longer than 24 hours.

- You agree to store files (such as images) for no longer than 24 hours\*.

<sub><sub>\* If you would like further consideration or questions, please contact us at api@muzooka.com.</sub></sub>

## Restful API
For the most current version of our API please view the [v2 documentation](v2.md)

## Webhooks
You can integrate your server with Muzooka by utilizing webhooks. Read more in a dedicated [webhook integration guide](webhooks.md).
