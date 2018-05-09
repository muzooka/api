# Muzooka API

First contact us to get an authentication token to access the API. Email us at api@muzooka.com to request a token.

Once the authentication token is recieved it must be sent in an http header called `X-muzooka-auth-token` for all requests to the API

## Artist Lookup Endpoint

To lookup an artist, use their name or a portion of it for a fuzzy match. Use following endpoint:
`GET` `https://api.muzooka.com/artists`

Supported query parameters are:

* `name`: Will perform a fuzzy match on the part of the name.
* `nameStartsWith`: Will look for artists who's name starts with a given term.
* `nameMatch`: Will perform an exact match on the artist name.
* `limit`: Will paginate the result in pages of given size. Maximum page limit is 100, default limit is 25.
* `offset`: To select certain page of results, set an offset. This will skip given number of records from the top of the list.

Note that ony one name matching parameter can be used at the time. Having a name matching parameter is a requirement to access this endpoint.

Result would contain two top-level fileds: `data` and `pages`. `data` is an array of results, `pages` is the information about pagination.

### Example Response
```json
{
    "data": [
        {
            "name": "Paul McCartney",
            "banner": {
                "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124081/small.jpg",
                "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124081/medium.jpg",
                "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124081/large.jpg",
                "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/124081/original.jpg"
            },
            "profile": {
                "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124082/small.jpg",
                "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124082/medium.jpg",
                "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/124082/large.jpg",
                "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/124082/original.jpg"
            },
            "facebookUsername": "PaulMcCartney",
            "city": "Liverpool",
            "province": null,
            "website": "http://www.PaulMcCartney.com",
            "about": "Page administered by [MPL] ",
            "description": "Paul McCartney's official Facebook page. ",
            "socialLinks": [
                {
                    "type": "twitter",
                    "id": "PaulMcCartney",
                    "url": "https://twitter.com/PaulMcCartney"
                },
                {
                    "type": "facebook",
                    "id": "PaulMcCartney",
                    "url": "https://www.facebook.com/PaulMcCartney"
                },
                {
                    "type": "youtube",
                    "id": "PAULMCCARTNEY",
                    "url": "https://www.youtube.com/channel/PAULMCCARTNEY"
                }
            ],
            "links": {
                "video": "https://api.muzooka.com/artists/PaulMcCartney/videos",
                "images": "https://api.muzooka.com/artists/PaulMcCartney/images",
                "muzookaUrl": "https://muzooka.com/PaulMcCartney"
            }
        }
    ],
    "pages": {
        "total": 1,
        "totalPages": 1
    }
}
```

## Artist Endpoint

The following endpoint returns the artists data
`GET` `https://api.muzooka.com/artists/:facebookUsername`

### Response Structure

* `name`: Artist name
* `city`: City the artist resides in
* `province`: Province or state the artist resides in
* `country`: Country the artist resides in
* `website`: Artist website
* `about`: About the artist
* `description`: Description of the artist
* `facebookUsername`: Artist's username on facebook. If artist does not have a username on facebook, artist's numeric facebook ID would be provided.
* `banner`: Banner image of the artist
* - `smallUrl`: Small version of the Banner
* - `mediumUrl`: Medium version of the Banner
* - `largeUrl`: Large version of the Banner
* - `original`: Original version of the Banner
* `profile`: Profile image of the artist
* - `smallUrl`: Small version of Profile image
* - `mediumUrl`: Medium version of Profile image
* - `largeUrl`: Large version of Profile image
* - `original`: Original version of Profile image
* `socialLinks`: An array of social media links, only existing social links for the given artist will be included
* - `type`: Type of social media link (ex Twitter)
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
    "about": "'Songs of Experience' released Dec 1, pre-order now and listen to new song Get Out Of Your Own Way. eXPERIENCE + iNNOCENCE US Tour opens May.  http://www.u2.com\n\n",
    "description": "'Songs of Experience' released Dec 1, pre-order now and listen to new song Get Out Of Your Own Way. eXPERIENCE + iNNOCENCE US Tour opens May.  http://www.u2.com",
    "banner": {
        "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/small.jpg",
        "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/medium.jpg",
        "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/large.jpg",
        "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/40841/original.jpg"
    },
    "profile": {
        "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/55072/small.jpg",
        "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/55072/medium.jpg",
        "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/55072/large.jpg",
        "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/55072/original.jpg"
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
        "video": "https://api.muzooka.com/artists/u2/videos",
        "images": "https://api.muzooka.com/artists/u2/images",
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

const muzookaAuthToken = 'EXTSyU^BAxK#ukJ$@aS5mj3z';
const config = {
  baseURL: 'https://api.muzooka.com/',
  headers: {
    'X-muzooka-auth-token': muzookaAuthToken,
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

$response = \Httpful\Request::get('https://api.muzooka.com/artists/U2')
    ->addHeader('X-muzooka-auth-token', 'EXTSyU^BAxK#ukJ$@aS5mj3z')
    ->expectsJson()
    ->send();

echo($response->body->name); //U2
?>
```

## Artist Video Endpoint

The following endpoint returns the videos for the artist

`GET` `https://api.muzooka.com/artists/:facebookUsername/videos`

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

`GET` `https://api.muzooka.com/artists/:facebookUsername/images`

Muzooka API provides 3 fixed-width resized version of the original image, along with the original image. Muzooka images are not crops, just resizes – so only the width is of knows size and aspect ratio is preserved of the original image. This applied to all images across the API, not just to this endpoint.

Common sizes used throughout the API are `small`, `medium`, `large` and `original`. Here is a size chart:

- `small`: 320 px wide.
- `medium`: 768 px wide.
- `large`: 1200 px wide.
- `original`: original image as initally uploaded.

### Response Structure
Array of: 
 - `id`: Muzooka image Id
 - `smallUrl`: The url for the small image
 - `mediumUrl`: The url for the large image
 - `largeUrl`: The url for the large image
 - `original`: The url for the original image

### Example Response
```json
[
  {
    "id": "123",
    "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/small.jpg",
    "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/medium.jpg",
    "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/large.jpg",
    "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/original.jpg"
  },
  {
    "id": "456",
    "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/small.jpg",
    "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/medium.jpg",
    "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/large.jpg",
    "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/original.jpg",
  }
]
```
