import requests
from data.activity.endpoint import ActivityEndpoint
from utils.metadata.params import Params
from utils.variables import HEADERS


def _transform_url(url: str, params: Params):
    if url == ActivityEndpoint.TOKEN_ACTIVITY.value:
        url = url.format(params.token)
        params.token = None

    return url, params


def get_response(url: str, params: Params):
    url, params = _transform_url(url, params)
    _response = requests.get(
        url=url,
        params=params,
        headers=HEADERS,
    )
    return _response.json()
