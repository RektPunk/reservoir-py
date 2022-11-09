from utils.enum_variables import HasValueEnum


class AttributesEndpoint(HasValueEnum):
    ALL_ATTRIBUTES: str = (
        "https://api.reservoir.tools/collections/{0}/attributes/all/v2"
    )
    ALL_ATTRIBUTES_TOKEN_IDS: str = (
        "https://api.reservoir.tools/collections/{0}/attributes/static/v1"
    )
    EXPLORE_ATTRIBUTES: str = (
        "https://api.reservoir.tools/collections/{0}/attributes/explore/v3"
    )
