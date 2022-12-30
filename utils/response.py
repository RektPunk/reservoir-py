from typing import Any, List, Dict, Tuple
import requests
from data.activity.endpoint import ActivityEndpoint
from data.attributes.endpoint import AttributesEndpoint
from data.collections.endpoint import CollectionsEndpoint
from data.orders.endpoint import OrdersEndpoint
from data.owners.endpoint import OwnersEndpoint
from utils.metadata.params import Params
from utils.variables import HEADERS, CONTINUATION, StatusCode


def _transform_url(url: str, params: Params) -> Tuple[str, Params]:
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
    elif OrdersEndpoint.has_value(url):
        if url == OrdersEndpoint.BID_DISTRIBUTION.value:
            url = url.format(params.collection)
            params.collection = None
    elif OwnersEndpoint.has_value(url):
        if url == OwnersEndpoint.OWNERS_COLLECTION_DISTRIBUTION.value:
            url = url.format(params.collection)
            params.collection = None
        elif url == OwnersEndpoint.OWNERS_COLLECTION_SET_DISTRIBUTION.value:
            url = url.format(params.collectionsSetId)
            params.collectionsSetId = None
    return url, params


def get_response(url: str, params: Params) -> Dict[str, Any]:
    url, params = _transform_url(url, params)
    _response = requests.get(
        url=url,
        params=params,
        headers=HEADERS,
    )
    if _response.status_code == StatusCode._200.value:
        return _response.json()
    else:
        raise Exception(f"status code: {_response.status_code}")


def get_bulk_response(
    url: str,
    params: Params,
    max_continuation: int = 10,
) -> List[Dict[str, Any]]:
    response_list: List = []
    if CONTINUATION not in params.dict().keys():
        return get_response(url, params)

    _continuation = None
    for _ in range(max_continuation):
        params.continuation = _continuation
        _response = get_response(url, params)
        response_list.append(_response)
        if (
            _response.get(CONTINUATION) is None
            or _response.get(CONTINUATION) == _continuation
        ):
            break
        else:
            _continuation = _response.get(CONTINUATION)
    return response_list
