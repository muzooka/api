# Webhook Integration Guide

Webhooks allow you to subscribe to changes in Muzooka database and receive notifications about changes as soon as they occur without having to poll for changes through the REST endpoints.

Whenever a change happens on one of the entities your server is subscribed to, Muzooka is going to deliver a HTTP POST to your server with updated data, just as if you would be requesting it through a REST endpoint request.

Webhooks can be used to do a real-time updates without periodical polling, cache invalidations and many other purposes.

Webhook calls do not count towards your API call rate limit (but do have their own limits), so by using both technologies you can achieve much more then using only one of those.

## Installing a webhook

Before requests can be sent to your server, Muzooka needs to know where to deliver the data and what entities you are interested in.

Process of subscribing your URL to a certain type of Muzooka updates is called webhook installation and you'd need to do it once per data type/URL pair.

You can have multiple enpoints notified about same object: to do that you'd need two separate installations.

Your usage plan has limits for number of installations. Having multiple endpoint notified for same object counts towards  your plan limits as multiple calls.

To install a webhook you need to make a POST request to Muzooka server with parameters of your subscription.

As with the rest of the Muzooka API, you need an active API token to make requests. You can request one in [Muzooka Developer section](https://app.muzooka.com/m/developers) if you don't have one already.

To install a new webhook, you need to send a POST request to https://devapi.muzooka.com/v2/webhooks with JSON-formatted request body containing parameters "type", "filter" and "url".

Webhook is defined by it's `type` and `filter` parameters.

`type` is the type of object inside Muzooka that you are interested in. Currently, following types are supported:
- `page`

More types may be added in future.

`filter` if the filtering pattern that is applied when any object of specified `type` was changed to determine if your URL should be notified. For type `page` it is page's Facebook username. Example: when you specify `type: page` and `filter: u2`, your URL will get notifications every time U2's Muzooka page will be changed.

To authenticate with Muzooka API, provide your token with `X-api-key` HTTP header.

Example with cURL:

```
curl -X POST https://devapi.muzooka.com/v2/webhooks \
  -H 'Content-Type: application/json' \
  -H 'X-api-key: REPLACE_THIS_WITH_YOUR_API_KEY' \
  -d '{
    "type": "page",
    "filter": "u2",
    "url": "https://webhook.site/0ea7ede9-f354-5f32-9230-9ac2a54e45c5"
}'
```

Response structure is in JSON.
Success result has HTTP status 200 and body `{"message":"ok"}`.
Error result has HTTP status other than 200 and body similar to `{"message":"error description goes here"}`.

After creating a webhook, you would start receiving notifications right away, so generally it makes sense to set up your server first and install the webhook as the last step.

Muzooka server will check your URL before installing a webhook. In order to result in success, your server has to respond with HTTP status 200 within 3 seconds with a body not larger than 32Kb (preferably empty). Such check request will have no data (empty body).

Currently, webhooks do not expire, but do count the number of failed requests. If too many requests fail consecutively for the webhook, webhook may become uninstalled automatically.


## Uninstalling a webhook

Uninstalling a webhook is necessary to keep your webhook count below the usage limit. You may want to unsubscribe from changes that do not need real time updates anymore (remember you can always request same data from REST endpoints) to allow new subscriptions for other objects in Muzooka to be created.

To uninstall a webhook, send JSON-formatted HTTP DELETE request to `https://devapi-qc.muzooka.com/v2/webhooks/:Webhookid` where `:Webhookid` is the UUID of the webhook in question.

Here is a cURL example:
```
curl -X DELETE https://devapi.muzooka.com/v2/webhooks/cdse9sa2-4fa4-65d9-85e2-501064efdb00 \
  -H 'x-api-key: REPLACE_THIS_WITH_YOUR_API_KEY'
```

Response structure is in JSON.
Success result has HTTP status 200 and body `{"message":"ok"}`.
Error result has HTTP status other than 200 and body similar to `{"message":"error description goes here"}`.

## Good practices

- Respond as quickly as possible. Muzooka server will wait for HTTP status 200 from your server for 3 seconds before declaring webhook call a failed attempt, so it makes sense to design your app in a way where it would respond to Muzooka call right away before handling any business logic (i.e. updating caches, etc).

- Respond with an empty body. Less data to transfer is always faster, and once installed, webhooks do not really need any data from your server apart from receiving confirmation (HTTP status 200). Muzooka webhook server will count any response that is larger than 32kb as a failed delivery attempt.

- Have a plan B. If your server would not be able to receive webhook notifications for prolonged period of time (datacenter outages, domain name changes, etc) - by the time you're up and running, some of the data may be out of date. Consider implementing re-fetching of critical data from Muzooka REST API once your server is back online.

