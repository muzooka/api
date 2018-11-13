# Muzooka API

## How To Request An API Key

1. Login to [Muzooka](https://www.muzooka.com/m/login).
2. Verify your Facebook account and permissions, you will be directed to the Page Manager.
3. On the left navigation, click [Developer](https://www.muzooka.com/m/developers).
4. In the top right, click the blue `Request API Key` button.
5. Once approved you will receive an email from Muzooka, [login](https://www.muzooka.com/m/login) and return to the [Developer](https://www.muzooka.com/m/developers) section.
6. To attain your key, click on `Click to reveal key`.

## API Usage & Terms of Service

The key must be sent in an http header called `X-api-key` for all requests to the API.

In order to use the API, you need to accept and comply with [Muzooka Terms of Service](https://www.muzooka.com/m/legal). Making requests to the API is considered as an act of accepting these terms:

- You agree to cache the JSON response for no longer than 24 hours.

- You agree to store files (such as images) for no longer than 24 hours\*.

<sub><sub>\* If you would like further consideration or questions, please contact us at api@muzooka.com.</sub></sub>

## Webhooks

You can integrate your server with Muzooka by utilizing webhooks. Read more in a dedicated [webhook integration guide](webhooks.md).

## Artist Lookup Endpoint

To lookup an artist, use their name or a portion of it for a fuzzy match. Use following endpoint:
`GET` `https://devapi.muzooka.com/v1/artists`

Supported query parameters are:

* `name`: Will perform a search the name.
* `limit`: Will paginate the result in pages of given size. Maximum page limit is 100, default limit is 25.
* `offset`: To select certain page of results, set an offset. This will skip given number of records from the top of the list.

Result would contain two top-level fileds: `data` and `pages`. `data` is an array of results, `pages` is the information about pagination.
Along with the artist data a `searchScore` is returned, the higher the value the more likely the result correlates with the artist name provided. The `isAboveConfidenceThreshold` boolean value simply marks the result as being above a threshold Muzooka has calculated internally. Results are always returned with the highest scoring artists first. In most cases if the first result has a `isAboveConfidenceThreshold` value of `true` then that result is the correct artist for the given artist name.

### Example Response
```json
{
    "name": "U2",
    "banner": {
        "smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/small.jpg",
        "landscape1x1smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/1x1/small.jpg",
        "landscape4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/4x3/small.jpg",
        "portrait4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/4x3/small.jpg",
        "landscape16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/16x9/small.jpg",
        "portrait16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/16x9/small.jpg",
        "landscape21x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/21x9/small.jpg",
        "mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/medium.jpg",
        "landscape1x1mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/1x1/medium.jpg",
        "landscape4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/4x3/medium.jpg",
        "portrait4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/4x3/medium.jpg",
        "landscape16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/16x9/medium.jpg",
        "portrait16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/16x9/medium.jpg",
        "landscape21x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/21x9/medium.jpg",
        "largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/large.jpg",
        "landscape1x1largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/1x1/large.jpg",
        "landscape4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/4x3/large.jpg",
        "portrait4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/4x3/large.jpg",
        "landscape16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/16x9/large.jpg",
        "portrait16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/portrait/16x9/large.jpg",
        "landscape21x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/109150/landscape/21x9/large.jpg",
        "original": "https://d53lufxrpjz6n.cloudfront.net/images/109150/original.jpg"
    },
    "profile": {
        "smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/small.jpg",
        "landscape1x1smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/small.jpg",
        "landscape4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/small.jpg",
        "portrait4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/small.jpg",
        "landscape16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/small.jpg",
        "portrait16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/small.jpg",
        "landscape21x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/small.jpg",
        "mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/medium.jpg",
        "landscape1x1mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/medium.jpg",
        "landscape4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/medium.jpg",
        "portrait4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/medium.jpg",
        "landscape16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/medium.jpg",
        "portrait16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/medium.jpg",
        "landscape21x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/medium.jpg",
        "largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/large.jpg",
        "landscape1x1largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/large.jpg",
        "landscape4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/large.jpg",
        "portrait4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/large.jpg",
        "landscape16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/large.jpg",
        "portrait16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/large.jpg",
        "landscape21x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/large.jpg",
        "original": "https://d53lufxrpjz6n.cloudfront.net/images/103194/original.jpg"
    },
    "facebookUsername": "u2",
    "city": "Dublin",
    "province": "County Dublin",
    "country": " Ireland",
    "website": "http://www.u2.com/",
    "bio": "U2 are an Irish rock band from Dublin formed in 1976. The group consists of Bono (lead vocals and rhythm guitar), the Edge (lead guitar, keyboards, and backing vocals), Adam Clayton (bass guitar), and Larry Mullen Jr. (drums and percussion).",
    "socialLinks": [
        {
            "type": "twitter",
            "id": "u2",
            "url": "https://twitter.com/u2"
        },
        {
            "type": "facebook",
            "id": "u2",
            "url": "https://www.facebook.com/u2"
        },
        {
            "type": "instagram",
            "id": "u2",
            "url": "https://www.instagram.com/u2"
        },
        {
            "type": "spotify",
            "id": null,
            "url": "https://open.spotify.com/artist/51Blml2LZPmy7TTiAg47vQ"
        },
        {
            "type": "youtube",
            "id": "u2official",
            "url": "https://www.youtube.com/channel/u2official"
        },
        {
            "type": "iheartradio",
            "id": "u2-970/",
            "url": "https://www.iheart.com/artist/u2-970/"
        },
        {
            "type": "bandsintown",
            "id": "U2",
            "url": "https://www.bandsintown.com/U2"
        },
        {
            "type": "soundcloud",
            "id": "u2",
            "url": "https://www.soundcloud.com/u2"
        }
    ],
    "links": {
        "video": "https://devapi.muzooka.com/v1/artists/u2/videos",
        "images": "https://devapi.muzooka.com/v1/artists/u2/images",
        "muzookaUrl": "https://www.muzooka.com/u2"
    }
}
```

## Artist Endpoint

The following endpoint returns the artists data
`GET` `https://devapi.muzooka.com/v1/artists/:facebookUsername`

### Response Structure

* `name`: Artist name
* `city`: City the artist resides in
* `province`: Province or state the artist resides in
* `country`: Country the artist resides in
* `website`: Artist website
* `bio`: A biographical summary about the artist
* `facebookUsername`: Artist's username on facebook. If artist does not have a username on facebook, artist's numeric facebook ID would be provided.
* `banner`: Banner image of the artist
* `profile`: Profile image of the artist
* `socialLinks`: An array of social media links, only existing social links for the given artist will be included
* - `type`: Type of social media link (for example, `twitter`)
* - `id`: Social media id, username or profile
* - `url`: Direct link to social media account
* `links`: Collection of endpoints
* - `videos`: Endpoint for artist videos
* - `images`: Endpoint for images the artist have uploaded
* - `performances`: Endpoint for upcoming performances for the artist (Not Implemented)
* - `muzookaUrl`: The Artist page on Muzooka.com

### Example Response
```json
{
    "name": "U2",
    "city": "Dublin",
    "province": null,
    "country": " Ireland",
    "website": "http://www.u2.com/",
    "bio": "U2 are an Irish rock band from Dublin formed in 1976. The group consists of Bono (lead vocals and rhythm guitar), the Edge (lead guitar, keyboards, and backing vocals), Adam Clayton (bass guitar), and Larry Mullen Jr. (drums and percussion).",
    "banner": {
        "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/small.jpg",
        "landscape1x1smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/1x1/small.jpg",
        "landscape4x3smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/4x3/small.jpg",
        "landscape16x9smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/16x9/small.jpg",
        "landscape21x9smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/21x9/small.jpg",
        "portrait4x3smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/4x3/small.jpg",
        "portrait16x9smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/16x9/small.jpg",
        "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/medium.jpg",
        "landscape1x1mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/1x1/medium.jpg",
        "landscape4x3mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/4x3/medium.jpg",
        "landscape16x9mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/16x9/medium.jpg",
        "landscape21x9mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/21x9/medium.jpg",
        "portrait4x3mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/4x3/medium.jpg",
        "portrait16x9mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/16x9/medium.jpg",
        "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/large.jpg",
        "landscape1x1largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/1x1/large.jpg",
        "landscape4x3largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/4x3/large.jpg",
        "landscape16x9largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/16x9/large.jpg",
        "landscape21x9largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/landscape/21x9/large.jpg",
        "portrait4x3largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/4x3/large.jpg",
        "portrait16x9largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/portrait/16x9/large.jpg",
        "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/original.jpg"
    },
    "profile": {
        "smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/small.jpg",
        "landscape1x1smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/1x1/small.jpg",
        "landscape4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/4x3/small.jpg",
        "portrait4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/4x3/small.jpg",
        "landscape16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/16x9/small.jpg",
        "portrait16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/16x9/small.jpg",
        "landscape21x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/21x9/small.jpg",
        "mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/medium.jpg",
        "landscape1x1mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/1x1/medium.jpg",
        "landscape4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/4x3/medium.jpg",
        "portrait4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/4x3/medium.jpg",
        "landscape16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/16x9/medium.jpg",
        "portrait16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/16x9/medium.jpg",
        "landscape21x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/21x9/medium.jpg",
        "largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/large.jpg",
        "landscape1x1largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/1x1/large.jpg",
        "landscape4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/4x3/large.jpg",
        "portrait4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/4x3/large.jpg",
        "landscape16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/16x9/large.jpg",
        "portrait16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/portrait/16x9/large.jpg",
        "landscape21x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/34653/landscape/21x9/large.jpg",
        "original": "https://d53lufxrpjz6n.cloudfront.net/images/34653/original.jpg"
    },
    "facebookUsername": "u2",
    "socialLinks": [
        {
            "type": "twitter",
            "id": "U2",
            "url": "https://twitter.com/U2"
        },
        {
            "type": "facebook",
            "id": "u2",
            "url": "https://www.facebook.com/u2"
        },
        {
            "type": "instagram",
            "id": "U2",
            "url": "https://www.instagram.com/U2"
        },
        {
            "type": "spotify",
            "id": null,
            "url": "https://open.spotify.com/artist/51Blml2LZPmy7TTiAg47vQ"
        },
        {
            "type": "youtube",
            "id": "UCpd21W3qWyzIl8-PXvyDA2g",
            "url": "https://www.youtube.com/channel/UCpd21W3qWyzIl8-PXvyDA2g"
        },
        {
            "type": "bandsintown",
            "id": "U2",
            "url": "https://www.bandsintown.com/U2"
        }
    ],
    "links": {
        "video": "https://devapi.muzooka.com/v1/artists/u2/videos",
        "images": "https://devapi.muzooka.com/v1/artists/u2/images",
        "muzookaUrl": "https://muzooka.com/u2"
    }
}
```

### Social Links

Currently, `socialLinks` field can have following types:

    - twitter
    - facebook
    - instagram
    - spotify
    - youtube
    - bandsintown
    - soundcloud
    - iheartradio
    - mixcloud
    - homepage
    - ticketmaster
    - lastfm
    - itunes
    - wiki
    - vevo

More types can be added in the future.


### Example – NODE.JS

```js
const axios = require('axios');

const muzookaAPIKey = 'EXTSyU^BAxK#ukJ$@aS5mj3z';
const config = {
  baseURL: 'https://devapi.muzooka.com/v1/',
  headers: {
    'X-api-key': muzookaAPIKey,
  },
};

const getArtist = facebookUsername =>
  axios.get(`artists/${facebookUsername}`, config)
    .then(({ data }) => data);
```

### Example – PHP

The following example uses PHP and the library [Httpful](http://phphttpclient.com/) installed with [Phar](http://php.net/manual/en/book.phar.php)

```php
<?php
include('./httpful.phar');

$response = \Httpful\Request::get('https://devapi.muzooka.com/v1/artists/U2')
    ->addHeader('X-api-key', 'EXTSyU^BAxK#ukJ$@aS5mj3z')
    ->expectsJson()
    ->send();

echo($response->body->name); //U2
?>
```

## Artist Video Endpoint

The following endpoint returns the videos for the artist

`GET` `https://devapi.muzooka.com/v1/artists/:facebookUsername/videos`

### Response Structure
Array of: 
 - `id`: Muzooka video id
 - `name`: Video name
 - `url`: The url of the video
 - `isFeatured`: Is set to `true` for a featured video, otherwise if `false`
 - `videoId`: The YouTube id of the video
 - `embed`: The embed url of the video
### Example Response
```json
[
  {
    "id": "123",
    "name": "U2 - Song For Someone (Directed by Matt Mahurin)",
    "url": "https://youtu.be/RFjcd_d2PhY",
    "isFeatured": false,
    "videoId": "RFjcd_d2PhY",
    "embed": "https://www.youtube.com/embed/RFjcd_d2PhY"
  },
  {
    "id": "456",
    "name": "U2 - I Still Haven't Found What I'm Looking For",
    "url": "https://youtu.be/e3-5YC_oHjE",
    "isFeatured": true,
    "videoId": "e3-5YC_oHjE",
    "embed": "https://www.youtube.com/embed/e3-5YC_oHjE"
  }
]
```
### Artist Images Endpoint

The following endpoint returns the images for the artist

`GET` `https://devapi.muzooka.com/v1/artists/:facebookUsername/images`

Muzooka API provides multiple variants of every image. There are two variant types: a resize and a crop. Resize has the same aspect ratio as the original image, whereas crops have standard aspect ratios. This applies to all images across the API, not just to this endpoint.

Currently, Muzooka supports following aspect ratios:
- `1x1`
- `4x3`
- `16x9`
- `21x9`

Each crop variant can be presented in either `landscape` or `portrait` orientation. Square images (`1x1`), by convention, do not have a `portrait` variant. Also there is no `portrait` orientation for `21x9`.

There are 4 standard sizes, along with the original image, that Muzooka API serves:
- `small`: 320x240 in `4x3`, 320x180 in `16x9`, 320x135 in `21x9`
- `medium`: 768x576 in `4x3`, 768x432 in `16x9`, 768x324 in `21x9`
- `large`: 1280x960 in `4x3`, 1280x720 in `16x9`, 1280x540 in `21x9`
- `original`: original image as initally uploaded.

### Response Structure
Array of: 
- `id`: Muzooka image Id
- `type`: The type of image (banner or profile)
- `source`: Where the image originated
- `isPrimary`: The primary image for the given type 
- `smallUrl`: A small resize of the original image with aspect ratio preserved
- `landscape1x1smallUrl`: Landscape crop with 1x1 aspect ratio, 320x320
- `landscape4x3smallUrl`: Landscape crop with 4x3 aspect ratio, 320x240
- `landscape16x9smallUrl`: Landscape crop with 16x9 aspect ratio, 320x180
- `landscape21x9smallUrl`: Landscape crop with  aspect ratio, 320x135
- `portrait4x3smallUrl`: Portrait crop with 4x3 aspect ratio, 240x320
- `portrait16x9smallUrl`: Portrait crop with 16x9 aspect ratio, 180x320
- `mediumUrl`: A medium resize of the original image with aspect ratio preserved
- `landscape1x1mediumUrl`: Landscape crop with 1x1 aspect ratio, 768x768
- `landscape4x3mediumUrl`: Landscape crop with  aspect ratio, 768x576
- `landscape16x9mediumUrl`: Landscape crop with 16x9 aspect ratio, 768x432
- `landscape21x9mediumUrl`: Landscape crop with  aspect ratio, 768x324
- `portrait4x3mediumUrl`: Portrait crop with 4x3 aspect ratio, 576x768
- `portrait16x9mediumUrl`: Portrait crop with 16x9 aspect ratio, 432x768
- `largeUrl`: A large resize of the original image with aspect ratio preserved
- `landscape1x1largeUrl`: Landscape crop with 1x1 aspect ratio, 1280x1280
- `landscape4x3largeUrl`: Landscape crop with 4x3 aspect ratio, 1280x960
- `landscape16x9largeUrl`: Landscape crop with 16x9 aspect ratio, 1280x720
- `landscape21x9largeUrl`: Landscape crop with  aspect ratio, 1280x540
- `portrait4x3largeUrl`: Portrait crop with 4x3 aspect ratio, 960x1280
- `portrait16x9largeUrl`: Portrait crop with 16x9 aspect ratio, 720x1280
- `original`: The original uploaded image

### Example Response
```json
[
  {
      "smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/small.jpg",
      "landscape1x1smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/1x1/small.jpg",
      "landscape4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/4x3/small.jpg",
      "portrait4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/4x3/small.jpg",
      "landscape16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/16x9/small.jpg",
      "portrait16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/16x9/small.jpg",
      "landscape21x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/21x9/small.jpg",
      "mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/medium.jpg",
      "landscape1x1mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/1x1/medium.jpg",
      "landscape4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/4x3/medium.jpg",
      "portrait4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/4x3/medium.jpg",
      "landscape16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/16x9/medium.jpg",
      "portrait16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/16x9/medium.jpg",
      "landscape21x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/21x9/medium.jpg",
      "largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/large.jpg",
      "landscape1x1largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/1x1/large.jpg",
      "landscape4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/4x3/large.jpg",
      "portrait4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/4x3/large.jpg",
      "landscape16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/16x9/large.jpg",
      "portrait16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/portrait/16x9/large.jpg",
      "landscape21x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/106327/landscape/21x9/large.jpg",
      "original": "https://d53lufxrpjz6n.cloudfront.net/images/106327/original.jpg",
      "id": 106327,
      "type": "banner",
      "source": "facebook",
      "isPrimary": false
  },
  {
      "smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/small.jpg",
      "landscape1x1smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/small.jpg",
      "landscape4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/small.jpg",
      "portrait4x3smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/small.jpg",
      "landscape16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/small.jpg",
      "portrait16x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/small.jpg",
      "landscape21x9smallUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/small.jpg",
      "mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/medium.jpg",
      "landscape1x1mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/medium.jpg",
      "landscape4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/medium.jpg",
      "portrait4x3mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/medium.jpg",
      "landscape16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/medium.jpg",
      "portrait16x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/medium.jpg",
      "landscape21x9mediumUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/medium.jpg",
      "largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/large.jpg",
      "landscape1x1largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/1x1/large.jpg",
      "landscape4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/4x3/large.jpg",
      "portrait4x3largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/4x3/large.jpg",
      "landscape16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/16x9/large.jpg",
      "portrait16x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/portrait/16x9/large.jpg",
      "landscape21x9largeUrl": "https://d53lufxrpjz6n.cloudfront.net/images/103194/landscape/21x9/large.jpg",
      "original": "https://d53lufxrpjz6n.cloudfront.net/images/103194/original.jpg",
      "id": 103194,
      "type": "profile",
      "source": "facebook",
      "isPrimary": true
  },
  ...
]
```
