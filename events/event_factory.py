from datetime import datetime
from model.task import TaskInfo
from model.enums import EventCode
from .base_event import Event

class EventFactory:
    @staticmethod
    def create_event(
        event_info: TaskInfo, 
        location_point_id: int,
        event_code: EventCode,
        event_time: datetime
    ) -> Event:
        if event_code == EventCode.START_PROCESSING:
            from .start_processing_event import StartProcessingEvent
            return StartProcessingEvent(event_info, location_point_id, event_code, event_time)
        
        elif event_code == EventCode.END_PROCESSING:
            from .end_processing_event import EndProcessingEvent
            return EndProcessingEvent(event_info, location_point_id, event_code, event_time)
        
        elif event_code == EventCode.DETECTION:
            from .detection_event import DetectionEvent
            return DetectionEvent(event_info, location_point_id, event_code, event_time)
        
        elif event_code == EventCode.APPEARANCE:
            from .appearance_event import AppearanceEvent
            return AppearanceEvent(event_info, location_point_id, event_code, event_time)

        raise ValueError(f"Unknown event code: {event_code}")