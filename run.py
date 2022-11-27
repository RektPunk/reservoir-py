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
from data.events import (
    EventsEndpoint,
    AsksStatusChangesParams,
    BidStatusChangesParams,
    CollectionFloorChangesParams,
    CollectionTopBidChangesParams,
)
from data.orders import (
    OrdersEndpoint,
    BidDistributionParams,
)
from data.sales import SalesEndpoint, SalesParams
from utils.response import get_bulk_response


TEST_COLLECTION = "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"
TEST_USER = "0xef764bac8a438e7e498c2e5fccf0f174c3e3f8db"
TEST_TOKEN = "9998"


all_activity_params = AllActivityParams()
all_activity_response = get_bulk_response(
    url=ActivityEndpoint.ALL_ACTIVITY.value,
    params=all_activity_params,
)

collection_activity_params = CollectionActivityParams(collection=TEST_COLLECTION)
collection_activity_response = get_bulk_response(
    url=ActivityEndpoint.COLLECTION_ACTIVITY.value,
    params=collection_activity_params,
)


user_activity_params = UserActivityParams(
    users=TEST_USER,
    types=["sale", "transfer"],
)
user_activity_response = get_bulk_response(
    url=ActivityEndpoint.USER_ACTIVITY.value,
    params=user_activity_params,
)


token_activity_params = TokenActivityParams(
    token=f"{TEST_COLLECTION}:{TEST_TOKEN}",
    types=["sale", "transfer"],
)
token_activity_response = get_bulk_response(
    url=ActivityEndpoint.TOKEN_ACTIVITY.value,
    params=token_activity_params,
)


all_attributes_params = AllAttributesParams(collection=TEST_COLLECTION)
all_attributes_response = get_bulk_response(
    url=AttributesEndpoint.ALL_ATTRIBUTES.value, params=all_attributes_params
)


all_attributes_token_ids_params = AllAttributesTokenIdsParams(
    collection=TEST_COLLECTION
)
all_attributes_token_ids_response = get_bulk_response(
    url=AttributesEndpoint.ALL_ATTRIBUTES_TOKEN_IDS.value,
    params=all_attributes_token_ids_params,
)


explore_attributes_params = ExploreAttributesParams(
    collection=TEST_COLLECTION,
)
explore_attributes_response = get_bulk_response(
    url=AttributesEndpoint.EXPLORE_ATTRIBUTES.value,
    params=explore_attributes_params,
)

collections_params = CollectionsParams(
    id=TEST_COLLECTION,
)
collections_response = get_bulk_response(
    url=CollectionsEndpoint.COLLECTIONS.value,
    params=collections_params,
)

collections_source_stats_params = CollectionSourceStatsParams(
    collection=TEST_COLLECTION,
)
collections_source_stats_response = get_bulk_response(
    url=CollectionsEndpoint.COLLECTIONS_SOURCE_STATS.value,
    params=collections_source_stats_params,
)

search_collections_params = SearchCollectionsParams()
search_collections_response = get_bulk_response(
    url=CollectionsEndpoint.SEARCH_COLLECTIONS.value,
    params=search_collections_params,
)

user_collections_params = UserCollectionsParams(
    user=TEST_USER,
)

user_collections_response = get_bulk_response(
    url=CollectionsEndpoint.USER_COLLECTIONS.value, params=user_collections_params
)


sales_params = SalesParams(
    collection=TEST_COLLECTION,
)

sales_response = get_bulk_response(
    url=SalesEndpoint.SALES.value,
    params=sales_params,
)

asks_status_changes_params = AsksStatusChangesParams(contract=TEST_COLLECTION)

asks_status_changes_response = get_bulk_response(
    url=EventsEndpoint.ASKS_STATUS_CHANGES.value,
    params=asks_status_changes_params,
)

bid_status_changes_params = BidStatusChangesParams(contract=TEST_COLLECTION)

bid_status_changes_response = get_bulk_response(
    url=EventsEndpoint.BID_STATUS_CHANGES.value,
    params=bid_status_changes_params,
)

collection_floor_changes_params = CollectionFloorChangesParams(
    collection=TEST_COLLECTION
)

collection_floor_changes_response = get_bulk_response(
    url=EventsEndpoint.COLLECTION_FLOOR_CHANGES.value,
    params=collection_floor_changes_params,
)

collection_top_bid_changes_params = CollectionTopBidChangesParams(
    collection=TEST_COLLECTION
)

collection_top_bid_changes_response = get_bulk_response(
    url=EventsEndpoint.COLLECTION_TOP_BID_CHANGES.value,
    params=collection_top_bid_changes_params,
)

bid_distribution_params = BidDistributionParams(
    collection=TEST_COLLECTION,
)

bid_distribution_response = get_bulk_response(
    url=OrdersEndpoint.BID_DISTRIBUTION.value,
    params=bid_distribution_params,
)
