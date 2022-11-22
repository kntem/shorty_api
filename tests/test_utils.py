from os.path import join, dirname
from jsonschema import validate
import os
import json


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_schema(path):
    """This function loads the given schema available"""

    schema_file = open(os.path.join(__location__, path))
    schema = json.load(schema_file)
    return schema


def create_shortlinks_request_body(long_url, provider):
    return json.dumps({
        "url": long_url,
        "provider": provider
    })


def shortlinks_post(client, provider, long_url):
    data = create_shortlinks_request_body(long_url, provider)
    return client.post('/shortlinks', data=data, content_type='application/json')


def validate_shorty_response(client, provider, long_url):
    # Create
    response = shortlinks_post(client, provider, long_url)
    resp_json = json.loads(response.data)
    shortlinks_response_schema = get_schema("api_schemas/shortlinks_resp_schema.json")
    validate(instance=response, schema=shortlinks_response_schema)

    assert resp_json["url"] == long_url
