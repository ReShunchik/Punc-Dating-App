from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class Message:
    date_time : datetime
    sender_id : int
    reciver_id : int
    text : str
    attachments : List[str] = None
