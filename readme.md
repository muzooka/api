# Muzooka API

First contact us to get an authentication token to access the api

Once the authentication token is recieved it must be sent in an http header called `muzooka-auth-token` for all requests to the API

## Artist Endpoint

The following endpoint returns the artists data
`GET` `https://api.muzooka.com/artists/:facebookUsername`

### Response Structure

* `name`: artist name
* `city`: city the artist resides in
* `province`: province or state the artist resides in
* `country`: country the artist resides in
* `website`: artist website
* `about`: About the artist
* `bio`: Bio information for the artist
* `description`: Description of the artist
* `generalInfo`: General information on the artist
* `social` : collection of social media information
* - `twitter`: Twitter url for the artist
* - `facebook`: Facebook url for the artist
* - `instagram`: Instagram url for the artist
* - `spotify`: spotify url for the artist
* - `youtube`: Youtube Channel url for the artist
* - `iheartradio`: iHeartRadio url for the artist
* `links`: Collection of endpoints
* - `videos`: Endpoint for artist videos
* - `images`: Endpoint for images the artist have uploaded
* - `performances`: Endpoint for upcoming performances for the artist (Not Implemented)
* - `muzookaUrl`: The Artist page on Muzooka.com

### Example Response
```json
{
  "name": "U2",
  "city": "Dublin, Ireland",
  "province": null,
  "country": null,
  "website": "http://www.u2.com/",
  "about": "‘In the darkness where we learn to see…’\nhttp://www.u2.com/news/title/the-blackout\n\n",
  "bio": null,
  "description": "You're The Best Thing About Me, the first single from the new album Songs of Experience https://u2.lnk.to/BestThingFP",
  "generalInfo": null,
  "social": {
    "twitter": "https://twitter.com/U2",
    "facebook": "https://www.facebook.com/u2",
    "instagram": "https://www.instagram.com/U2",
    "spotify": "https://open.spotify.com/artist/51Blml2LZPmy7TTiAg47vQ",
    "youtube": "https://www.youtube.com/channel/UCpd21W3qWyzIl8-PXvyDA2g",
    "iheartradio": "https://www.iheart.com/artist/u2-970/"
  },
  "links": {
    "video": "http://api.muzooka.com/artists/u2/videos",
    "images": "http://api.muzooka.com/artists/u2/images",
    "performances": "http://api.muzooka.com/artists/u2/performances",
    "muzookaUrl": "https://www.muzooka.com/u2"
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
### Artist Images Endpoint

The following endpoint returns the images for the artist

`GET` `https://api.muzooka.com/artists/:facebookUsername/images`

### Response Structure
Array of: 
 - `smallUrl`: the url for the small image
 - `mediumUrl`: The url for the large image
 - `largeUrl`: the url for the large image
 - `original`: the url for the original image

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