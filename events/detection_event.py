from base_event import Event
from core.simulation import SimulationEngine
from model.enums import EventCode
from model.task import TaskInfo
from event_factory import EventFactory

class DetectionEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        next_points = simulation.paths.get(self.location_point_id, [])
        for next_point in next_points:
            task_info = TaskInfo(
                group_id = self.event_info.group_id,
                object_id = self.event_info.object_id,
                detector_id = self.location_point_id,
                source_id = self.location_point_id,
                relevance_time = self.event_info.relevance_time
            )
            new_event = EventFactory.create_event(
                event_info = task_info,
                location_point_id = next_point,
                event_code = EventCode.START_PROCESSING,
                event_time = self.event_time
            )
            simulation.add_event(new_event)