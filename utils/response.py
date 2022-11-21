from typing import Callable, List
import requests
from data.activity.endpoint import ActivityEndpoint
from data.attributes.endpoint import AttributesEndpoint
from data.collections.endpoint import CollectionsEndpoint
from utils.metadata.params import Params
from utils.variables import HEADERS, CONTINUATION


def _transform_url(url: str, params: Params):
    if ActivityEndpoint.has_value(url):
        if url == ActivityEndpoint.TOKEN_ACTIVITY.value:
            url = url.format(params.token)
            params.token = None
    elif AttributesEndpoint.has_value(url):
        url = url.format(params.collection)
        params.collection = None
    elif CollectionsEndpoint.has_value(url):
        if url == CollectionsEndpoint.USER_COLLECTIONS.value:
            url = url.format(params.user)
            params.user = None
    return url, params


def get_response(url: str, params: Params):
    url, params = _transform_url(url, params)
    _response = requests.get(
        url=url,
        params=params,
        headers=HEADERS,
    )
    return _response.json()


def get_bulk_response(
    url: str,
    params: Params,
    max_continuation: int = 10,
):
    response_list: List = []
    if CONTINUATION not in params.dict().keys():
        return get_response(url, params)

    _continuation = None
    for _ in range(max_continuation):
        params.continuation = _continuation
        _response = get_response(url, params)
        response_list.append(_response)
        if (
            _response[CONTINUATION] == _continuation
            or _response[CONTINUATION] is None
            or CONTINUATION not in _response.keys()
        ):
            break
        else:
            _continuation = _response[CONTINUATION]
    return response_list
