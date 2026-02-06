from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str
    status: str
    created_at: str
    deadline: Optional[str]