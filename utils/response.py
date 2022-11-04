import requests
from data.activity.endpoint import ActivityEndpoint
from data.attributes.endpoint import AttributesEndpoint
from utils.metadata.params import Params
from utils.variables import HEADERS


def _transform_url(url: str, params: Params):
    if ActivityEndpoint.has_value(url):
        if url == ActivityEndpoint.TOKEN_ACTIVITY.value:
            url = url.format(params.token)
            params.token = None
    elif AttributesEndpoint.has_value(url):
        url = url.format(params.collection)
        params.collection = None
    return url, params


def get_response(url: str, params: Params):
    url, params = _transform_url(url, params)
    _response = requests.get(
        url=url,
        params=params,
        headers=HEADERS,
    )
    return _response.json()
