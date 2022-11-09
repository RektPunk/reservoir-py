from typing import Union, List
from pydantic import conint, validator
from utils.metadata.params import Params
from utils.enum_variables import CollcectionsSortByEnum
from utils.validators import (
    string_to_list_validator,
    has_value_validator,
    contract_conflict_validator,
)


class CollectionsParams(Params):
    id: str = None
    slug: str = None
    collectionsSetId: str = None
    community: str = None
    contract: Union[str, List[str]] = None
    name: str = None
    includeTopBid: bool = False
    includeAttributes: bool = None
    includeOwnerCount: bool = None
    sortBy: str = CollcectionsSortByEnum.allTimeVolume.value
    limit: conint(ge=1, le=20) = 20
    continuation: str = None

    @validator("contract")
    def contract_validator(cls, v, values):
        _v = string_to_list_validator(v)
        return contract_conflict_validator(_v, values, key="id")

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, CollcectionsSortByEnum)


class CollectionSourceStatsParams(Params):
    collection: str


class SearchCollectionsParams(Params):
    name: str = None
    community: str = None
    collectionsSetId: str = None
    limit: conint(ge=1, le=50) = 20


class UserCollectionsParams(Params):
    user: str
    community: str = None
    collectionsSetId: str = None
    collection: str = None
    includeTopBid: bool = False
    includeLiquidCount: bool = False
    offset: conint(ge=0, le=10000) = 0
    limit: conint(ge=1, le=100) = 20
