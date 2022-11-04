from enum import Enum


class ActivityEndpoint(Enum):
    ALL_ACTIVITY: str = "https://api.reservoir.tools/activity/v3"
    COLLECTION_ACTIVITY: str = "https://api.reservoir.tools/collections/activity/v4"
    USER_ACTIVITY: str = "https://api.reservoir.tools/users/activity/v4"
    TOKEN_ACTIVITY: str = "https://api.reservoir.tools/tokens/token/activity/v3"
