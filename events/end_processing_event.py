from .base_event import Event
from core.simulation import SimulationEngine
from model.enums import EventCode
from model.task import TaskInfo
from .event_factory import EventFactory

class EndProcessingEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        current_point = self.location_point_id
        state = simulation.points[current_point]
        next_task = state.finish()

        if next_task:
            new_event = EventFactory.create_event(
                event_info = next_task,
                location_point_id = current_point,
                event_code = EventCode.START_PROCESSING,
                event_time = self.event_time
            )
            simulation.add_event(new_event)

        next_points = simulation.paths.get(self.location_point_id, [])
        for point in next_points:
            task_info = TaskInfo(
                group_id = self.event_info.group_id,
                object_id = self.event_info.object_id,
                detector_id = self.event_info.detector_id,
                source_id = current_point,
                relevance_time = self.event_info.relevance_time
            )
            new_event = EventFactory.create_event(
                event_info = task_info,
                location_point_id = point,
                event_code = EventCode.START_PROCESSING,
                event_time = self.event_time
            )
            simulation.add_event(new_event)