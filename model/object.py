from dataclasses import dataclass
from datetime import datetime

@dataclass
class Object:
    group_id: int
    object_id: int
    appearance_time: datetime
    relevance_time: datetime