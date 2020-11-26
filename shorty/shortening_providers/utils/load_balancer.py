from shorty.shortening_providers.bitly import Bitly
from shorty.shortening_providers.tinyurl import TinyUrl

class ShorteningProvidersLoadBalancer:

    @staticmethod
    def get_balanced_provider():
