from datetime import datetime
from utils.generate_time import generate_time

class Sensor:
    def __init__(self, start_detection: datetime, last_detection: datetime, distribution_id: int, expected_value: float, variance: float):
        self.start_detection = start_detection
        self.last_detection = last_detection
        self.distribution_id = distribution_id
        self.expected_value = expected_value
        self.variance = variance
        self.discovered = set()

    def detect(self, objects):
        detected_object = None
        for obj in objects:
            object_id = obj.object_id
            if object_id not in self.discovered:
                self.discovered.add(object_id) 
                detected_object = obj
        return detected_object
    
    def get_next_trigger(self):
        delay = generate_time(self.distribution_id, self.expected_value, self.variance)
        self.last_detection = self.last_detection + delay
        return self.last_detection