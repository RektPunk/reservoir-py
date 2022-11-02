from typing import Optional
from utils.params import Params


class AllActivityParams(Params):
    includeMetadata: bool = False
    limit: int = 20
    continuation: Optional[str] = None
