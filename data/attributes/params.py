from pydantic import validator
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
    maxFloorAskPrices: int = 1
    maxLastSells: int = 0
    sortBy: str = AttributesSortByEnum.floorAskPrice.value
    offset: int = 0
    limit: int = 20

    @validator("sortBy")
    def sortby_validator(cls, v):
        return has_value_validator(v, AttributesSortByEnum)
