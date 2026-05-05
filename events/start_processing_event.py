from base_event import Event
from core.simulation import SimulationEngine
from model.processing_point import ProcessingPoint
from end_processing_event import EndProcessingEvent
from model.enums import EventCode

class StartProcessingEvent(Event):
    def make_event(self, simulation: SimulationEngine):
        current_point = self.location_point_id
        
        processing_point = simulation.system_state[current_point]

        task_info = self.event_info

        if processing_point.enter(task_info):
            processing_delay = simulation.points[current_point].generate_time()
            end_time = self.event_time + processing_delay
            simulation.add_event(EndProcessingEvent(task_info, current_point, EventCode.END_PROCESSING, end_time))