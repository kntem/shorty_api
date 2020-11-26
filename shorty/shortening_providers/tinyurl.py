import urllib
import requests
from shorty.shortening_providers.provider_conf import provider_config


class TinyUrl:
    def __init__(self):
        return

    @staticmethod
    def shorten_url(url_long):
        api_url_base = provider_config["tinyurl"]["api_url"]
        api_url = \
            api_url_base + "?" + urllib.parse.urlencode({"url": url_long})
        response = requests.get(api_url)
        response.raise_for_status()
        return response.text
