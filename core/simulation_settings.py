from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple
from model.processing_point import ProcessingPoint

@dataclass
class SimulationConfig:
    start: datetime
    end: datetime
    intensity: float
    stream_distribution_id: int
    stream_variance: float
    sensors: Dict[int, Dict]
    points: Dict[int, ProcessingPoint]
    paths: Dict[int, List[int]]
    groups: Dict[int, Tuple[int, int]]