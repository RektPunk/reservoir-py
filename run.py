from data.activity import (
    ActivityEndpoint,
    AllActivityParams,
    CollectionActivityParams,
    UserActivityParams,
    TokenActivityParams,
)
from data.attributes import (
    AttributesEndpoint,
    AllAttributesParams,
    AllAttributesTokenIdsParams,
    ExploreAttributesParams,
)
from data.collections import (
    CollectionsEndpoint,
    CollectionsParams,
    CollectionSourceStatsParams,
    SearchCollectionsParams,
    UserCollectionsParams,
)
from utils.response import get_response


TEST_COLLECTION = "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"
TEST_USER = "0xef764bac8a438e7e498c2e5fccf0f174c3e3f8db"
TEST_TOKEN = "9998"

all_activity_params = AllActivityParams()
all_activity_response = get_response(
    url=ActivityEndpoint.ALL_ACTIVITY.value,
    params=all_activity_params,
)

collection_activity_params = CollectionActivityParams(collection=TEST_COLLECTION)
collection_activity_response = get_response(
    url=ActivityEndpoint.COLLECTION_ACTIVITY.value,
    params=collection_activity_params,
)


user_activity_params = UserActivityParams(
    users=TEST_USER,
    types=["sale", "transfer"],
)
user_activity_response = get_response(
    url=ActivityEndpoint.USER_ACTIVITY.value,
    params=user_activity_params,
)


token_activity_params = TokenActivityParams(
    token=f"{TEST_COLLECTION}:{TEST_TOKEN}",
    types=["sale", "transfer"],
)
token_activity_response = get_response(
    url=ActivityEndpoint.TOKEN_ACTIVITY.value,
    params=token_activity_params,
)


all_attributes_params = AllAttributesParams(collection=TEST_COLLECTION)
all_attributes_response = get_response(
    url=AttributesEndpoint.ALL_ATTRIBUTES.value, params=all_attributes_params
)


all_attributes_token_ids_params = AllAttributesTokenIdsParams(
    collection=TEST_COLLECTION
)
all_attributes_token_ids_response = get_response(
    url=AttributesEndpoint.ALL_ATTRIBUTES_TOKEN_IDS.value,
    params=all_attributes_token_ids_params,
)


explore_attributes_params = ExploreAttributesParams(
    collection=TEST_COLLECTION,
)
explore_attributes_response = get_response(
    url=AttributesEndpoint.EXPLORE_ATTRIBUTES.value,
    params=explore_attributes_params,
)

collections_params = CollectionsParams(
    id=TEST_COLLECTION,
)
collections_response = get_response(
    url=CollectionsEndpoint.COLLECTIONS.value,
    params=collections_params,
)

collections_source_stats_params = CollectionSourceStatsParams(
    collection=TEST_COLLECTION,
)
collections_source_stats_response = get_response(
    url=CollectionsEndpoint.COLLECTIONS_SOURCE_STATS.value,
    params=collections_source_stats_params,
)

search_collections_params = SearchCollectionsParams()
search_collections_response = get_response(
    url=CollectionsEndpoint.SEARCH_COLLECTIONS.value,
    params=search_collections_params,
)

user_collections_params = UserCollectionsParams(
    user=TEST_USER,
)

user_collections_response = get_response(
    url=CollectionsEndpoint.USER_COLLECTIONS.value, params=user_collections_params
)
