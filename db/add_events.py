import psycopg2
from psycopg2.extras import execute_values
from settings import DB_CONFIG
from typing import List, Tuple

def add_events(data: List[Tuple]):
    query = """
        INSERT INTO messages (group_id, object_id, detector_id, source_id, location_point_id, action_id, action_time)
        VALUES %s
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            execute_values(cursor, query, data)
            conn.commit()