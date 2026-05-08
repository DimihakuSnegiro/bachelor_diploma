from datetime import datetime
from core.simulation import SimulationEngine, SimulationHistory
from core.simulation_settings import SimulationConfig
from model.processing_point import ProcessingPoint

start_time = datetime(2026, 5, 6, 16, 10, 0)
end_time = datetime(2026, 5, 6, 18, 10, 0)

groups = {
    1: (1, 5),
    2: (6, 10)
}

paths = {
    1: [2],
    2: [3, 4],
    3: [],
    4: []
}

sensors = {
    1: {"sensor_name": "Датчик 1"}
}

points = {
    2: ProcessingPoint(1, 1, 1, 1),
    3: ProcessingPoint(1, 1, 1, 1),
    4: ProcessingPoint(1, 1, 1, 1)
}

simulation_config = SimulationConfig(
    start = start_time,
    end = end_time,
    intensity = 0.5,
    stream_distribution_id = 1,
    stream_variance = 0.0,
    sensors = sensors,
    points = points,
    paths = paths,
    groups = groups
)

history = SimulationHistory()
engine = SimulationEngine(simulation_config, history)
engine.run_simulation()