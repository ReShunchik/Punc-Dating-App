from dataclasses import dataclass
from typing import List
from Message import Message

@dataclass
class Dialog:
    user1_id : int
    user2_id : int
    is_terminated : bool
    messages : List[Message] = None


    def add_message(self, new_message):
        self.messages.append(new_message)

    def remove_message(self, deleted_message):
        self.messages.remove(deleted_message)