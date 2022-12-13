from utils.enum_variables import HasValueEnum


class OwnersEndpoint(HasValueEnum):
    OWNERS: str = "https://api.reservoir.tools/owners/v1"
    COMMON_COLLECTION: str = "https://api.reservoir.tools/owners/common-collections/v1"
    OWNERS_INTERSECTION: str = "https://api.reservoir.tools/owners/cross-collections/v1"
    OWNERS_COLLECTION_DISTRIBUTION: str = (
        "https://api.reservoir.tools/collections/{0}/owners-distribution/v1"
    )
    OWNERS_COLLECTION_SET_DISTRIBUTION: str = (
        "https://api.reservoir.tools/collections-sets/{0}/owners-distribution/v1"
    )
