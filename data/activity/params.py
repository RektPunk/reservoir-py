from typing import Optional, List, Union
from pydantic import validator
from utils.metadata.params import Params
from utils.variables import ActivitySortByEnum, ActivityTypesEnum
from utils.validators import string_to_list_validator, has_value_validator


class AllActivityParams(Params):
    includeMetadata: bool = False
    limit: int = 20
    continuation: Optional[str] = None


class CollectionActivityParams(Params):
    collection: str
    collectionsSetId: str = None
    community: str = None
    limit: int = 20
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    continuation: Optional[str] = None


class UserActivityParams(Params):
    users: Union[str, List[str]]
    collection: str = None
    collectionsSetId: str = None
    community: str = None
    limit: int = 20
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = ActivityTypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("users")
    def users_validator(cls, v):
        return string_to_list_validator(v)

    @validator("types")
    def types_validator(cls, v):
        _v = string_to_list_validator(v)
        return has_value_validator(_v, ActivityTypesEnum)


class TokenActivityParams(Params):
    token: str
    limit: int = 20
    sortBy: str = ActivitySortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = ActivityTypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("types")
    def types_validator(cls, v):
        _v = string_to_list_validator(v)
        return has_value_validator(_v, ActivityTypesEnum)
