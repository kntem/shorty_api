from shorty.shortening_providers.bitly import Bitly


class TestBitlyPRovider:
    def test_happy_path(self):
        short_url1 = Bitly.shorten_url("https://withplum.com/")
        short_url2 = Bitly.shorten_url("https://withplum.com/")
        assert short_url1 == short_url1
