from abc import ABC, abstractmethod
from datetime import datetime
from model.task import TaskInfo
from model.enums import EventCode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.simulation import SimulationEngine

class Event(ABC):
    event_count = 0

    def __init__(self, event_info: TaskInfo, location_point_id: int, event_code: EventCode, event_time: datetime):
        self.event_info = event_info
        self.location_point_id = location_point_id
        self.event_code = event_code
        self.event_time = event_time
        Event.event_count += 1
        self.order = Event.event_count

    def __eq__(self, other):
        return self.event_time == other.event_time and self.order == other.order
    
    def __lt__(self, other):
        if self.event_time != other.event_time:
            return self.event_time < other.event_time
        return self.order < other.order

    def to_tuple(self):
        return (
            self.event_info.group_id,
            self.event_info.object_id,
            self.event_info.detector_id,
            self.event_info.source_id,
            self.location_point_id,
            self.event_code.value,
            self.event_time
        )

    @abstractmethod
    def make_event(self, simulation: 'SimulationEngine'):
        pass