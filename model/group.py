from dataclasses import dataclass

@dataclass
class Group:
    start_object_id: int
    end_object_id: int
    distribution_id: int
    expected_lifetime: float
    variance_lifetime: float