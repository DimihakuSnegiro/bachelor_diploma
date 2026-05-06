import numpy as np
from datetime import timedelta

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