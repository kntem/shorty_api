Microservice called `shorty`, 
which supports two URL shortening providers: [bit.ly](https://dev.bitly.com/)
and [tinyurl.com](https://gist.github.com/MikeRogers0/2907534).
The service exposes a single endpoint: `POST /shortlinks`. 
The endpoint should receives a JSON with the following schema:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The URL to shorten                 |
| provider | string | N        | The provider to use for shortening |

The response should be a `Shortlink` resource containing:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The original URL                   |
| link     | string | Y        | The shortened link                 |

For example:
```json
{
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka"
}
```
