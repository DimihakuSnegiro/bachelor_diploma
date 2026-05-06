from .base_event import Event
from core.simulation import SimulationEngine
from model.enums import EventCode
from .event_factory import EventFactory

class StartProcessingEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        current_point = self.location_point_id
        
        processing_point = simulation.points[current_point]

        task_info = self.event_info

        if processing_point.enter(task_info):
            processing_delay = simulation.points[current_point].generate_time()
            end_time = self.event_time + processing_delay
            new_event = EventFactory.create_event(
                event_info = task_info,
                location_point_id = current_point,
                event_code = EventCode.END_PROCESSING,
                event_time = end_time
            )
            simulation.add_event(new_event)