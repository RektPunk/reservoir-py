from typing import Union, List
from pydantic import conint, validator
from utils.metadata.params import Params
from utils.validators import string_to_list_validator


class OwnersParams(Params):
    collectionsSetId: str = None
    collection: str = None
    contract: str = None
    token: str = None
    attributes: str = None
    offset: conint(ge=0) = 0
    limit: conint(ge=1, le=500) = 20


class CommonCollections(Params):
    owners: Union[str, List[str]]
    limit: conint(ge=1, le=50) = 20

    @validator("owners")
    def owners_validator(cls, v):
        return string_to_list_validator(v)


class OwnersIntersection(Params):
    collections: Union[str, List[str]]
    limit: conint(ge=1, le=50) = 20

    @validator("collections")
    def collections_validator(cls, v):
        return string_to_list_validator(v)


class OwnersCollectionDistributionParams(Params):
    collection: str


class OwnersCollectionSetDistributionParams(Params):
    collectionsSetId: str
