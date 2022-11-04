import os
from typing import Dict
from enum import Enum
from dotenv import load_dotenv


class HasValueEnum(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class ApiKey(Enum):
    load_dotenv()
    RESERVIOR_API_KEY: str = os.environ["RESERVIOR_API_KEY"]


class ActivitySortByEnum(HasValueEnum):
    eventTimestamp: str = "eventTimestamp"
    createdAt: str = "createdAt"


class AttributesSortByEnum(HasValueEnum):
    floorAskPrice: str = "floorAskPrice"
    topBidValue: str = "topBidValue"


class ActivityTypesEnum(HasValueEnum):
    sale: str = "sale"
    ask: str = "ask"
    transfer: str = "transfer"
    mint: str = "mint"
    bid: str = "bid"
    bid_cancel: str = "bid_cancel"
    ask_cancel: str = "ask_cancel"


HEADERS: Dict[str, str] = {"accept": "*/*", "x-api-key": ApiKey.RESERVIOR_API_KEY.value}
