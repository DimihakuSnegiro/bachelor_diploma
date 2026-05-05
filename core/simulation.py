from datetime import datetime, timedelta
from simulation_settings import SimulationConfig
from typing import List
import numpy as np
from events.base_event import Event
import heapq

class SimulationEngine:
    def __init__(self, settings: SimulationConfig):
        self.events_queue: List[Event] = []
        self.start = settings.start
        self.end = settings.end
        self.intensity = settings.intensity
        self.stream_distribution_id = settings.stream_distribution_id
        self.stream_expected_value = settings.stream_expected_value
        self.stream_variance = settings.stream_variance
        self.sensors = settings.sensors
        self.points = settings.points
        self.paths = settings.paths
        self.groups = settings.groups
    
    def add_event(self, new_event: Event):
        heapq.heappush(self.events_queue, new_event)