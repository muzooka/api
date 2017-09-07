First contact us to get an authentication token to access the api

Once the authentication token is recieved it must be sent in an http header called `muzooka-auth-token` for all requests to the API

### Band Endpoint
The following endpoint returns the band data
`GET` `https://api.muzooka.com/bands/:facebookUsername`

### Response Structure
* `name`: band name
* `city`: city the band resides in
* `province`: province or state the band resides in
* `country`: country the band resides in
* `social` : collection of social media information
* - `twitter`: Twitter username for the band
* - `facebook`: Facebook username for the band
* - `instagram`: Instagram username for the band
* - `spotify`: spotify username for the band
* - `youtube`: Youtube Channel for the band
* - `iHeartRadio`: iHeartRadio profile for the band
* `website`: Bands website
* `about`: About the band
* `bio`: Bio information for the band
* `description`: Description of the band
* `links`: Collection of endpoints
* - `videos`: Endpoint for bands videos
* - `images`: Endpoint for images the band have uploaded
*  - `performances`: Endpoint for upcoming performances for the band

### Example Response
```json
{
  "subdomain": "u2",
  "facebookUsername": "u2",
  "name": "U2",
  "city": "Dublin, Ireland",
  "province": null,
  "country": null,
  "social": {
    "twitter": "U2",
    "mixcloud": null,
    "instagram": "U2",
    "soundcloud": "",
    "spotify": "https://open.spotify.com/artist/51Blml2LZPmy7TTiAg47vQ",
    "youtube": "UCpd21W3qWyzIl8-PXvyDA2g",
    "iheartradio": null,
  }
  "website": "http://www.u2.com/news/title/the-joshua-tree-at-30",
  "about": "'I wanna feel sunlight on my face...' Marking 30 years of The Joshua Tree in stadiums across North America & Europe. Dates & Tickets - http://www.u2.com\n\n",
  "bio": null,
  "description": "'Only to be with you...' The Joshua Tree at Thirty. http://www.u2.com/news/title/the-joshua-tree-at-30",
  "generalInfo": null,
  "links": {
    "video": "/bands/u2/videos",
    "images": "/bands/u2/images",
    "performances": "/bands/u2/performances"
  }
}
```
### Example

The following example uses PHP and the library [Httpful](http://phphttpclient.com/) installed with [Phar](http://php.net/manual/en/book.phar.php)

```php
<?php
include('./httpful.phar');

$response = \Httpful\Request::get('https://api.muzooka.com/bands/U2')
    ->addHeader('muzooka-auth-token', 'EXTSyU^BAxK#ukJ$@aS5mj3z')
    ->expectsJson()
    ->send();

echo($response->body->name); //U2
?>
```

### Band Video Endpoint

The following endpoint returns the videos for the band

`GET` `https://api.muzooka.com/bands/:facebookUsername/videos`

### Response Structure
Array of: 
 - `name`: video name
 - `url`: The url of the video

### Example Response
```json
[
  {
    "name": "U2 - Song For Someone (Directed by Matt Mahurin)",
    "url" "https://youtu.be/RFjcd_d2PhY"
  },
  {
    "name": "U2 - I Still Haven't Found What I'm Looking For",
    "url": "https://youtu.be/e3-5YC_oHjE",

  }
]
```
### Band Images Endpoint

The following endpoint returns the images for the band

`GET` `https://api.muzooka.com/bands/:facebookUsername/images`

### Response Structure
Array of: 
 - `name`: video name
 - `url`: The url of the video

### Example Response
```json
[
  {
    "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/small.jpg",
    "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/medium.jpg",
    "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/large.jpg",
    "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/33111/original.jpg"
  },
  {
    "smallUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/small.jpg",
    "mediumUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/medium.jpg",
    "largeUrl": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/large.jpg",
    "original": "https://d1vuu6jk2dpw02.cloudfront.net/images/33631/original.jpg",
  }
]
```