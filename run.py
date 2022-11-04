from data.activity import (
    ActivityEndpoint,
    AllActivityParams,
    CollectionActivityParams,
    UserActivityParams,
    TokenActivityParams,
)
from utils.response import get_response


all_activity_params = AllActivityParams()
all_activity_response = get_response(
    url=ActivityEndpoint.ALL_ACTIVITY.value,
    params=all_activity_params,
)

collection_activity_params = CollectionActivityParams(
    collection="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
)
collection_activity_response = get_response(
    url=ActivityEndpoint.COLLECTION_ACTIVITY.value,
    params=collection_activity_params,
)


user_activity_params = UserActivityParams(
    users="0x2e50b23af9a31c1f56e0434bedeb35cd41b8df41",
    types=["sale", "transfer"],
)
user_activity_response = get_response(
    url=ActivityEndpoint.USER_ACTIVITY.value,
    params=user_activity_params,
)


token_activity_params = TokenActivityParams(
    token="0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb:4999",
    types=["sale", "transfer"],
)
token_activity_response = get_response(
    url=ActivityEndpoint.TOKEN_ACTIVITY.value,
    params=token_activity_params,
)
