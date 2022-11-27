from utils.enum_variables import HasValueEnum


class OrdersEndpoint(HasValueEnum):
    BID_DISTRIBUTION: str = "https://api.reservoir.tools/collections/{0}/top-bids/v1"
