from .base_event import Event
from model.enums import EventCode
from core.simulation import SimulationEngine
from model.task import TaskInfo
from .event_factory import EventFactory

class AppearanceEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        for sensor in simulation.sensors:
            task_info = TaskInfo(
                group_id = self.event_info.group_id,
                object_id = self.event_info.object_id,
                detector_id = None,
                source_id = None,
                relevance_time = self.event_info.relevance_time
            )
            new_event = EventFactory.create_event(
                event_info = task_info,
                location_point_id = sensor,
                event_code = EventCode.DETECTION,
                event_time = self.event_time
            )
            simulation.add_event(new_event)