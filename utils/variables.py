import os
from typing import Dict
from enum import Enum
from dotenv import load_dotenv


class ApiKey(Enum):
    load_dotenv()
    RESERVIOR_API_KEY: str = os.environ["RESERVIOR_API_KEY"]


class SortByEnum(Enum):
    eventTimestamp: str = "eventTimestamp"
    createdAt: str = "createdAt"


class TypesEnum(Enum):
    sale: str = "sale"
    ask: str = "ask"
    transfer: str = "transfer"
    mint: str = "mint"
    bid: str = "bid"
    bid_cancel: str = "bid_cancel"
    ask_cancel: str = "ask_cancel"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


HEADERS: Dict[str, str] = {"accept": "*/*", "x-api-key": ApiKey.RESERVIOR_API_KEY.value}
