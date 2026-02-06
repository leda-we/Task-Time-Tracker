from dataclasses import dataclass
from typing import Optional

@dataclass
class TimeEntry:
    id: Optional[int]
    task_id: int
    start_time: str
    end_time: str
    duration_minutes: int