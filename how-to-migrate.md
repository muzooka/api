# Migrate to thew new version of Muzooka's API
In order to make our API more feature rich, Muzooka is moving to a new set of REST endpoints. The old endpoints will continue to work until the end of August, 2018 at which point they will return 404 errors. In order to access the new endpoints two small changes are required to be made to your implementations:

  - The header `X-muzooka-auth-token` needs to be `X-api-key`
  - The endpoint `https://api.muzooka.com/artists` is now `https://devapi.muzooka.com/v1/artists`
