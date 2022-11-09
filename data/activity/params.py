from typing import Optional, List, Union
from pydantic import conint, validator, root_validator
from utils.metadata.params import Params
from utils.enum_variables import ActivitySortByEnum, ActivityTypesEnum
from utils.validators import (
    string_to_list_validator,
    has_value_validator,
    activity_limit_validator,
    conflict_validator,
)


class AllActivityParams(Params):
    includeMetadata: bool = False
    limit: conint(ge=1, le=1000) = 20
    continuation: Optional[str] = None


class CollectionActivityParams(Params):
    collection: str
    collectionsSetId: str = None
    community: str = None
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    continuation: Optional[str] = None
    limit: int = 20

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, ActivitySortByEnum)

    @validator("limit")
    def limit_validator(cls, v, values):
        return activity_limit_validator(v, values)

    @root_validator
    def mutual_conflict_validator(cls, values):
        return conflict_validator(
            values, keys=["collection", "collectionsSetId", "community"]
        )


class UserActivityParams(Params):
    users: Union[str, List[str]]
    collection: str = None
    collectionsSetId: str = None
    community: str = None
    limit: conint(ge=1, le=200) = 20
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = ActivityTypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("users")
    def users_validator(cls, v):
        return string_to_list_validator(v)

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, ActivitySortByEnum)

    @validator("types")
    def types_validator(cls, v):
        _v = string_to_list_validator(v)
        return has_value_validator(_v, ActivityTypesEnum)

    @root_validator
    def mutual_conflict_validator(cls, values):
        return conflict_validator(
            values, keys=["collection", "collectionsSetId", "community"]
        )


class TokenActivityParams(Params):
    token: str
    limit: conint(ge=1, le=20) = 20
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = ActivityTypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, ActivitySortByEnum)

    @validator("types")
    def types_validator(cls, v):
        _v = string_to_list_validator(v)
        return has_value_validator(_v, ActivityTypesEnum)
