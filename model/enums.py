from enum import Enum

class EventCode(Enum):
    APPEARANCE = 1
    DETECTION = 2
    WAITING_IN_QUEUE = 3
    START_PROCESSING = 4
    END_PROCESSING = 5