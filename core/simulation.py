from datetime import datetime
from .simulation_settings import SimulationConfig
from typing import List
from utils.generate_time import generate_time
from events.base_event import Event
from model.task import TaskInfo
from model.enums import EventCode
from events.event_factory import EventFactory
from db.add_events import add_events
import heapq

class SimulationHistory:
    def __init__(self, batch_size = 50_000):
        self.batch_size = batch_size
        self.event_log: List[tuple] = []

    def add_message(self, event: Event):
        self.event_log.append(event.to_tuple())
        if len(self.event_log) >= self.batch_size:
            self.flush()

    def flush(self):
        add_events(self.event_log)
        self.event_log = []

class SimulationEngine:
    def __init__(self, settings: SimulationConfig, event_history: SimulationHistory):
        self.events_queue: List[Event] = []
        self.event_history = event_history
        self.start = settings.start
        self.end = settings.end
        self.intensity = settings.intensity
        self.stream_distribution_id = settings.stream_distribution_id
        self.stream_variance = settings.stream_variance
        self.sensors = settings.sensors
        self.points = settings.points
        self.paths = settings.paths
        self.groups = settings.groups
    
    def add_event(self, new_event: Event):
        heapq.heappush(self.events_queue, new_event)

    def get_next_object_time(self, current_time: datetime) -> datetime:
        distribution_arrival = self.stream_distribution_id
        mean_inter_arrival = 1.0 / self.intensity
        variance_arrival = self.stream_variance

        delay = generate_time(distribution_arrival, mean_inter_arrival, variance_arrival)
        return current_time + delay

    def run_simulation(self):
            current_time = self.start
            for group_id, (object_start, object_end) in self.groups.items():
                object_id = object_start
                while object_id <= object_end:
                    current_time = self.get_next_object_time(current_time)
                    task_info = TaskInfo(
                        group_id = group_id,
                        object_id = object_id,
                        detector_id = None,
                        source_id = None,
                        relevance_time = current_time
                    )
                    new_event = EventFactory.create_event(
                        event_info = task_info,
                        location_point_id = None,
                        event_code = EventCode.APPEARANCE,
                        event_time = current_time
                    )
                    self.add_event(new_event)
                    object_id += 1
                
            while self.events_queue:
                event = heapq.heappop(self.events_queue)

                if event.event_time >= self.end:
                    break

                event.make_event(self)
                self.event_history.add_message(event)
            self.event_history.flush()