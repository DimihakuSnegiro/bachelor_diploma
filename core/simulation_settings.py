from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List
from model.processing_point import ProcessingPoint
from model.sensor import Sensor
from model.group import Group

@dataclass
class SimulationConfig:
    start: datetime
    end: datetime
    intensity: float
    stream_distribution_id: int
    stream_variance: float
    sensors: Dict[int, Sensor]
    points: Dict[int, ProcessingPoint]
    paths: Dict[int, List[int]]
    groups: Dict[int, Group]