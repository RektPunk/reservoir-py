from utils.enum_variables import HasValueEnum
from utils.variables import ACTIVITY_LIMIT_RANGE_INCLUDE_METADATA


def string_to_list_validator(v):
    if isinstance(v, str):
        return [v]
    elif isinstance(v, list):
        return v


def has_value_validator(v, enum: HasValueEnum):
    if isinstance(v, str):
        if enum.has_value(v):
            return v
        else:
            raise ValueError(f"input not in {enum._member_names_}")
    elif isinstance(v, list):
        if all([enum.has_value(_) for _ in v]):
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


def contract_conflict_validator(v, values, key: str):
    _key = values[key]
    if isinstance(v, list) and _key in v:
        raise ValueError(f"{key} and contract conflict")
    else:
        return v
