from enum import Enum
from utils.variables import ReservoirUrl


class ActivityUrl(Enum):
    ALL_ACTIVITY: str = f"{ReservoirUrl.RESERVOIR_URL}/activity/v3"
    COLLECTION_ACTIVITY: str = f"{ReservoirUrl.RESERVOIR_URL}/collections/activity/v4"
    USERS_ACTIVITY: str = f"{ReservoirUrl.RESERVOIR_URL}/users/activity/v4"
    TOKEN_ACTIVITY: str = f"{ReservoirUrl.RESERVOIR_URL}/tokens/token/activity/v3"
