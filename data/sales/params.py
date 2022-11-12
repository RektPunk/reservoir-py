from typing import Union, List
from pydantic import conint, validator, root_validator
from utils.metadata.params import Params
from utils.validators import (
    string_to_list_validator,
    conflict_validator,
)


class SalesParams(Params):
    collection: str = None
    token: str = None
    includeTokenMetadata: bool = None
    contract: Union[str, List[str]] = None
    attributes: str = None
    txHash: str = None
    startTimestamp: float = None
    endTimestamp: float = None
    limit: conint(ge=1, le=1000) = 100
    continuation: str = None

    @validator("contract")
    def contract_validator(cls, v):
        return string_to_list_validator(v)

    @root_validator
    def mutual_conflict_validator(cls, values):
        return conflict_validator(
            values, keys=["collection", "collectionsSetId", "community"]
        )
