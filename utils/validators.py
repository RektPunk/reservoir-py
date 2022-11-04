from utils.variables import HasValueEnum


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
        raise ValueError("input not in Enum")
