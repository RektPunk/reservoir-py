from utils.enum_variables import HasValueEnum


class CollectionsEndpoint(HasValueEnum):
    COLLECTIONS: str = "https://api.reservoir.tools/collections/v5"
    COLLECTIONS_SOURCE_STATS: str = "https://api.reservoir.tools/collections/sources/v1"
    SEARCH_COLLECTIONS: str = "https://api.reservoir.tools/search/collections/v1"
    USER_COLLECTIONS: str = "https://api.reservoir.tools/users/{0}/collections/v2"
