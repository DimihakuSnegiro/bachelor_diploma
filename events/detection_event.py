from .base_event import Event
from core.simulation import SimulationEngine
from model.enums import EventCode
from model.task import TaskInfo
from .event_factory import EventFactory

class DetectionEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        sensor = simulation.sensors[self.get_location()]
        detected_object = sensor.detect(simulation.objects)
        if detected_object:
            next_points = simulation.paths.get(self.location_point_id, [])
            for point in next_points:
                task_info = TaskInfo(
                    group_id = detected_object.group_id,
                    object_id = detected_object.object_id,
                    detector_id = sensor,
                    source_id = None,
                    relevance_time = detected_object.relevance_time
                )
                new_event = EventFactory.create_event(
                    event_info = task_info,
                    location_point_id = point,
                    event_code = EventCode.START_PROCESSING,
                    event_time = self.event_time
                )
                simulation.add_event(new_event)
        next_trigger_time = sensor.get_next_trigger()
        task_info = TaskInfo(
            group_id = None,
            object_id = None,
            detector_id = None,
            source_id = None,
            relevance_time = None
        )
        new_event = EventFactory.create_event(
            event_info = task_info,
            location_point_id = self.location_point_id,
            event_code = EventCode.DETECTION,
            event_time = next_trigger_time
        )
        simulation.add_event(new_event)