from pydantic import conint, validator
from utils.metadata.params import Params
from utils.enum_variables import EventsSortDirectionEnum
from utils.validators import has_value_validator


class AsksStatusChangesParams(Params):
    contract: str = None
    startTimestamp: float = None
    endTimestamp: float = None
    sortDirection: str = EventsSortDirectionEnum.desc.value
    continuation: str = None
    limit: conint(ge=1, le=1000) = 50

    @validator("sortDirection")
    def sortdirection_validator(cls, v):
        return has_value_validator(v, EventsSortDirectionEnum)


class BidStatusChangesParams(Params):
    contract: str = None
    startTimestamp: float = None
    endTimestamp: float = None
    sortDirection: str = EventsSortDirectionEnum.desc.value
    continuation: str = None
    limit: conint(ge=1, le=1000) = 50

    @validator("sortDirection")
    def sortdirection_validator(cls, v):
        return has_value_validator(v, EventsSortDirectionEnum)


class CollectionFloorChangesParams(Params):
    collection: str = None
    startTimestamp: float = None
    endTimestamp: float = None
    sortDirection: str = EventsSortDirectionEnum.desc.value
    continuation: str = None
    limit: conint(ge=1, le=1000) = 50

    @validator("sortDirection")
    def sortdirection_validator(cls, v):
        return has_value_validator(v, EventsSortDirectionEnum)


class CollectionTopBidChangesParams(Params):
    collection: str = None
    startTimestamp: float = None
    endTimestamp: float = None
    sortDirection: str = EventsSortDirectionEnum.desc.value
    continuation: str = None
    limit: conint(ge=1, le=1000) = 50

    @validator("sortDirection")
    def sortdirection_validator(cls, v):
        return has_value_validator(v, EventsSortDirectionEnum)
