from typing import Optional
from pydantic import BaseModel


class AllActivityInput(BaseModel):
    includeMetadata: bool = False
    limit: int = 20
    continuation: Optional[str] = None
