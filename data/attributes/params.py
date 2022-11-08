from pydantic import validator, conint
from utils.metadata.params import Params
from utils.variables import AttributesSortByEnum
from utils.validators import has_value_validator


class AllAttributesParams(Params):
    collection: str


class AllAttributesTokenIdsParams(Params):
    collection: str


class ExploreAttributesParams(Params):
    collection: str
    includeTopBid: bool = False
    attributeKey: str = None
    maxFloorAskPrices: conint(ge=1, le=20) = 1
    maxLastSells: conint(ge=0, le=20) = 0
    sortBy: str = AttributesSortByEnum.floorAskPrice.value
    offset: conint(ge=0, le=10000) = 0
    limit: conint(ge=1, le=5000) = 20

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, AttributesSortByEnum)
