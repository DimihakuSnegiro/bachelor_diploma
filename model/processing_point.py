import numpy as np
from datetime import timedelta
from collections import deque
from typing import Deque, Optional
from task import TaskInfo

class ProcessingPoint:
    def __init__(self, distribution_id: int, expected_value: float, variance: float, channels: int):
        self.distribution_id = distribution_id
        self.expected_value = expected_value
        self.variance= variance
        self.channels = channels
        self.busy_channels = 0
        self.queue: Deque[TaskInfo] = deque()

    def has_free_channel(self) -> bool:
        return self.busy_channels < self.channels
    
    def get_queue_size(self) -> int:
        return len(self.queue)
    
    def get_channels(self) -> int:
        return self.channels
    
    def generate_time(self):
        distribution_id = self.distribution_id
        expected_value = self.expected_value
        variance = self.variance
        processing_time = None
        match distribution_id:
            case 1:  # Детерминированное
                processing_time = expected_value
            case 2:  # Равномерное
                half_range = np.sqrt(3 * variance)
                processing_time = float(np.random.uniform(expected_value - half_range, expected_value + half_range))
            case 3:  # Экспоненциальное
                processing_time = float(np.random.exponential(expected_value))
            case 4:  # Нормальное
                processing_time = float(np.random.normal(expected_value, np.sqrt(variance)))
            case _:
                raise ValueError(f"Неизвестный distribution_id: {distribution_id}")
            
        return timedelta(minutes = processing_time)

    def enter(self, task: TaskInfo) -> bool:
        if self.has_free_channel():
            self.busy_channels += 1
            return True
        
        self.queue.append(task)
        return False
    
    def finish(self) -> Optional[TaskInfo]:
        self.busy_channels -= 1
        
        if self.queue:
            next_task =  self.queue.popleft()
            self.busy_channels += 1
            return next_task
        
        return None