from utils.enum_variables import HasValueEnum


class EventsEndpoint(HasValueEnum):
    ASKS_STATUS_CHANGES: str = "https://api.reservoir.tools/events/asks/v2"
    BID_STATUS_CHANGES: str = "https://api.reservoir.tools/events/bids/v1"
    COLLECTION_FLOOR_CHANGES: str = (
        "https://api.reservoir.tools/events/collections/floor-ask/v1"
    )
    COLLECTION_TOP_BID_CHANGES: str = (
        "https://api.reservoir.tools/events/collections/top-bid/v1"
    )
