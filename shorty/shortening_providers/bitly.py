import requests
import json
from shorty.shortening_providers.provider_conf import provider_config


class Bitly:
    def __init__(self):
        return

    @staticmethod
    def shorten_url(url):

        data = json.dumps({
            "long_url": url,
            "domain": "bit.ly"
        })

        url = provider_config["bitly"]["api_url"]
        token = provider_config["bitly"]["token"]

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
        response = requests.post(url, data, headers=headers)
        # TODO: handle errors

        response.raise_for_status()

        return response.json()['link']
