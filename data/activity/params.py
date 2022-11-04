from typing import Optional, List, Union
from pydantic import validator
from utils.metadata.params import Params
from utils.variables import SortByEnum, TypesEnum


class AllActivityParams(Params):
    includeMetadata: bool = False
    limit: int = 20
    continuation: Optional[str] = None


class CollectionActivityParams(Params):
    collection: str
    collectionsSetId: str = None
    community: str = None
    limit: int = 20
    sortBy: str = SortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    continuation: Optional[str] = None


class UserActivityParams(Params):
    users: Union[str, List[str]]
    collection: str = None
    collectionsSetId: str = None
    community: str = None
    limit: int = 20
    sortBy: str = SortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = TypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("users")
    def users_validator(cls, v):
        if isinstance(v, str):
            return [v]
        elif isinstance(v, list):
            return v

    @validator("types")
    def types_validator(cls, v):
        if isinstance(v, str):
            v = [v]
        if all([TypesEnum.has_value(a) for a in v]):
            return v
        else:
            raise ValueError("types not in TypesEnum")


class TokenActivityParams(Params):
    token: str
    limit: int = 20
    sortBy: str = SortByEnum.eventTimestamp.value
    includeMetadata: bool = True
    types: Union[str, List[str]] = TypesEnum.sale.value
    continuation: Optional[str] = None

    @validator("types")
    def types_validator(cls, v):
        if isinstance(v, str):
            v = [v]
        if all([TypesEnum.has_value(a) for a in v]):
            return v
        else:
            raise ValueError("types not in TypesEnum")
