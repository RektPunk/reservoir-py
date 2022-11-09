import os
from typing import Dict
from enum import Enum
from dotenv import load_dotenv


class ApiKey(Enum):
    load_dotenv()
    RESERVIOR_API_KEY: str = os.environ["RESERVIOR_API_KEY"]


HEADERS: Dict[str, str] = {"accept": "*/*", "x-api-key": ApiKey.RESERVIOR_API_KEY.value}

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
