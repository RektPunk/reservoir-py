import os
from typing import Dict
from enum import Enum
from dotenv import load_dotenv


class ApiKey(Enum):
    load_dotenv()
    RESERVOIR_API_KEY: str = os.environ["RESERVOIR_API_KEY"]


class StatusCode(int, Enum):
    _200: int = 200


HEADERS: Dict[str, str] = {
    "accept": "*/*",
    "x-api-key": ApiKey.RESERVOIR_API_KEY.value,
}
CONTINUATION: str = "continuation"
ACTIVITY_LIMIT_RANGE_INCLUDE_METADATA = {
    True: {
        "ge": 1,
        "le": 20,
    },
    False: {
        "ge": 1,
        "le": 1000,
    },
}
