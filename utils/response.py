import requests
from utils.metadata.params import Params
from utils.variables import HEADERS


def get_response(url: str, params: Params):
    _response = requests.get(
        url=url,
        params=params,
        headers=HEADERS,
    )
    return _response.json()
