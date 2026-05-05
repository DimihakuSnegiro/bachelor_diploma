from dataclasses import dataclass
from datetime import datetime

@dataclass
class TaskInfo:
    group_id: int
    object_id: int
    detector_id: int
    source_id: int
    relevance_time: datetime