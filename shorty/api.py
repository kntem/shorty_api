from flask import Blueprint, jsonify, request, abort
from shorty.shortening_providers.bitly import Bitly
from shorty.shortening_providers.tinyurl import TinyUrl

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink_post():
    """Shortens URL

    Shortens url using two shortening url services: bitly and tinyurl
    based on the json body

    POST param url_provider: url to shorten with the Shortening service provider
        type url_provider: json

        example:
        {
            "url": "http://www.facebook.com",
            "provider": "tinyurl"
        }
    """

    url_provider = request.get_json()
    if not url_provider:
        abort(422)

    # lets have case insensitive arguments
    url_provider = {
        key.lower(): value for key, value in url_provider.items()
    }

    if "url" not in url_provider:
        abort(422)

    long_url = url_provider["url"]

    # shortening provider arg is optional
    if "provider" in url_provider:
        provider = url_provider["provider"]
    else:
        # lets have bitly as a default
        provider = "bitly"

    shortened_url = ""
    try:
        if provider.lower() == "bitly":
            shortened_url = Bitly.shorten_url(long_url)
        elif provider.lower() == "tinyurl":
            shortened_url = TinyUrl.shorten_url(long_url)
    except Exception as e:
        abort(e.response.status_code, e)

    response = {
        "url": long_url,
        "link": shortened_url
    }

    return jsonify(response)


# Error Handlers

@api.errorhandler(400)
def handle_providers_bad_request(error):
    """
    Handles 400 errors raised by the api.
    """
    error = jsonify("Bad url to shorten")
    error.status_code = 400
    return error


@api.errorhandler(404)
def handle_providers_not_found(error):
    """
    Handles 404 errors raised by the api.
    """
    error = jsonify("Shortening provider is unavailable")
    error.status_code = 503
    return error


@api.errorhandler(422)
def handle_unprocessable_entity(error):
    """
    Handles 422 errors raised by the api.
    """
    error = jsonify("A URL to shorten was not provided")
    error.status_code = 422
    return error
