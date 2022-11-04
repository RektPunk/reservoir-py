from utils.variables import HasValueEnum


class ActivityEndpoint(HasValueEnum):
    ALL_ACTIVITY: str = "https://api.reservoir.tools/activity/v3"
    COLLECTION_ACTIVITY: str = "https://api.reservoir.tools/collections/activity/v4"
    USER_ACTIVITY: str = "https://api.reservoir.tools/users/activity/v4"
    TOKEN_ACTIVITY: str = "https://api.reservoir.tools/tokens/{0}/activity/v3"
