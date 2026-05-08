CREATE TABLE IF NOT EXISTS messages(
    message_id SERIAL PRIMARY KEY,
    group_id INT,
    object_id INT,
    detector_id INT,
    source_id INT,
    location_point_id INT,
    action_id INT,
    relevance_time TIMESTAMP,
    action_time TIMESTAMP
);