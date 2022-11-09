from utils.enum_variables import HasValueEnum


ACTIVITY_LIMIT_RANGE_INCLUDE_METADATA = {
    True: {
        "ge": 1,
        "le": 20,
    },
    False: {
        "ge": 1,
        "le": 1000,
    },
}


def string_to_list_validator(v):
    if isinstance(v, str):
        return [v]
    elif isinstance(v, list):
        return v


def has_value_validator(v, enum: HasValueEnum):
    if isinstance(v, str):
        v = [v]
    if all([enum.has_value(a) for a in v]):
        return v
    else:
        raise ValueError(f"input not in {enum._member_names_}")


def activity_limit_validator(v, values):
    _include_metadata = values["includeMetadata"]
    _ge = ACTIVITY_LIMIT_RANGE_INCLUDE_METADATA[_include_metadata]["ge"]
    _le = ACTIVITY_LIMIT_RANGE_INCLUDE_METADATA[_include_metadata]["le"]
    if v >= _ge and v < _le:
        return v
    else:
        raise ValueError(f"limit not in {_ge} and {_le}")
