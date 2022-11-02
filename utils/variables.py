import os
from typing import Dict
from enum import Enum
from dotenv import load_dotenv


class ApiKey(Enum):
    load_dotenv()
    RESERVIOR_API_KEY: str = os.environ["RESERVIOR_API_KEY"]


HEADERS: Dict[str, str] = {"accept": "*/*", "x-api-key": ApiKey.RESERVIOR_API_KEY.value}
