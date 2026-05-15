from datetime import datetime

from core.simulation import SimulationEngine, SimulationHistory
from core.simulation_settings import SimulationConfig

from model.processing_point import ProcessingPoint
from model.group import Group
from model.sensor import Sensor


start_time = datetime(2026, 5, 6, 16, 10, 0)
end_time = datetime(2026, 5, 6, 18, 10, 0)

groups = {
    1: Group(
        start_object_id=1,
        end_object_id=5,
        distribution_id=1,
        expected_lifetime=30.0,
        variance_lifetime=5.0
    ),
    2: Group(
        start_object_id=6,
        end_object_id=10,
        distribution_id=1,
        expected_lifetime=45.0,
        variance_lifetime=10.0
    )
}

paths = {
    1: [2],
    2: [3, 4],
    3: [],
    4: []
}

sensors = {
    1: Sensor(
        start_detection=start_time,
        last_detection=start_time,
        distribution_id=1,
        expected_value=5.0,
        variance=1.0
    )
}

points = {
    2: ProcessingPoint(
        distribution_id=1,
        expected_value=3.0,
        variance=1.0,
        channels=1
    ),
    3: ProcessingPoint(
        distribution_id=1,
        expected_value=4.0,
        variance=1.0,
        channels=1
    ),
    4: ProcessingPoint(
        distribution_id=1,
        expected_value=2.0,
        variance=1.0,
        channels=1
    )
}

simulation_config = SimulationConfig(
    start=start_time,
    end=end_time,
    intensity=0.5,
    stream_distribution_id=1,
    stream_variance=0.0,
    sensors=sensors,
    points=points,
    paths=paths,
    groups=groups
)

history = SimulationHistory()

engine = SimulationEngine(
    settings=simulation_config,
    event_history=history
)

engine.run_simulation()