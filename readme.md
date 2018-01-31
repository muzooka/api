# Muzooka API

First contact us to get an authentication token to access the api

Once the authentication token is recieved it must be sent in an http header called `muzooka-auth-token` for all requests to the API

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
* `banner`: Banner image of the artist
* - `smallUrl`: Small version of the Banner
* - `mediumUrl`: Medium version of the Banner
* - `largeUrl`: Large version of the Banner
* - `original`: Original version of the Banner
* `social` : collection of social media information _Deprecated_ ❌
* - `twitter`: Twitter url for the artist
* - `facebook`: Facebook url for the artist
* - `instagram`: Instagram url for the artist
* - `spotify`: spotify url for the artist
* - `youtube`: Youtube Channel url for the artist
* - `iheartradio`: iHeartRadio url for the artist
* - `bandsintown`: Bands In Town url for the artist
* - `soundcloud`: Soundcloud url for the artist
* - `mixcloud`: Mixcloud url for the artist
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
    "social": {
        "twitter": {
            "url": "https://twitter.com/U2",
            "username": "U2"
        },
        "facebook": {
            "url": "https://www.facebook.com/u2",
            "username": "u2"
        },
        "instagram": {
            "url": "https://www.instagram.com/U2",
            "username": "U2"
        },
        "spotify": "https://open.spotify.com/artist/51Blml2LZPmy7TTiAg47vQ",
        "youtube": {
            "url": "https://www.youtube.com/channel/UCpd21W3qWyzIl8-PXvyDA2g",
            "channel": "UCpd21W3qWyzIl8-PXvyDA2g"
        },
        "iheartradio": {
            "url": "https://www.iheart.com/artist/",
            "profile": ""
        },
        "bandsintown": {
            "url": "https://www.bandsintown.com/U2",
            "username": "U2"
        },
        "mixcloud": {
            "url": "https://www.mixcloud.com/",
            "username": ""
        },
        "soundcloud": {
            "url": "https://www.soundcloud.com/",
            "username": ""
        }
    },
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
        "video": "https://api-qc.muzooka.com/artists/u2/videos",
        "images": "https://api-qc.muzooka.com/artists/u2/images",
        "muzookaUrl": "https://qc.muzooka.com/u2"
    }
}
```
### Example

The following example uses PHP and the library [Httpful](http://phphttpclient.com/) installed with [Phar](http://php.net/manual/en/book.phar.php)

```php
<?php
include('./httpful.phar');

$response = \Httpful\Request::get('https://api.muzooka.com/artists/U2')
    ->addHeader('muzooka-auth-token', 'EXTSyU^BAxK#ukJ$@aS5mj3z')
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
    "url" "https://youtu.be/RFjcd_d2PhY",
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
