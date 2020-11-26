from shorty.shortening_providers.provider_conf import provider_config
from tests.test_utils import validate_shorty_response, shortlinks_post
import pytest
import json

providers = provider_config.keys()


@pytest.mark.shorty_api
def test_shorty_happy(client):
    long_url = "https://withplum.com"
    for provider in providers:
        validate_shorty_response(client, provider, long_url)


@pytest.mark.shorty_api
def test_shorty_wrong_url(client):
    long_url = "a_url_that_doesnt_exist"
    for provider in providers:
        response = shortlinks_post(client, provider, long_url)
        assert response.status_code == 400


@pytest.mark.shorty_api
def test_shorty_empty_request_body(client):
    empty_req_body = json.dumps({})
    for provider in providers:
        response = client.post('/shortlinks', data=empty_req_body, content_type='application/json')
        # json.loads(response.data)
        assert response.status_code == 422
