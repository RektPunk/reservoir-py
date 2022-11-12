from enum import Enum


class HasValueEnum(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class ActivitySortByEnum(HasValueEnum):
    eventTimestamp: str = "eventTimestamp"
    createdAt: str = "createdAt"


class AttributesSortByEnum(HasValueEnum):
    floorAskPrice: str = "floorAskPrice"
    topBidValue: str = "topBidValue"


class ActivityTypesEnum(HasValueEnum):
    sale: str = "sale"
    ask: str = "ask"
    transfer: str = "transfer"
    mint: str = "mint"
    bid: str = "bid"
    bid_cancel: str = "bid_cancel"
    ask_cancel: str = "ask_cancel"


class CollcectionsSortByEnum(HasValueEnum):
    oneDayVolume: str = "1DayVolume"
    sevenDayVolume: str = "7DayVolume"
    thirtyDayVolume: str = "30DayVolume"
    allTimeVolume: str = "allTimeVolume"
    createdAt: str = "createdAt"
    floorAskPrice: str = "floorAskPrice"


class EventsSortDirectionEnum(HasValueEnum):
    asc: str = "asc"
    desc: str = "desc"
