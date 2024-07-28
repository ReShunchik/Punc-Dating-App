from dataclasses import dataclass
from typing import List
import Dialog

@dataclass
class Profile:
    user_id: int
    is_banned: bool
    age: int
    gender: str
    faculty: str
    live_in_dormitory: bool
    bio: str
    interests: List[str]

    def update_profile(self, age: int, gender: str, faculty: str, live_in_dormitory: bool,
                       bio: str,interests: List[str],):
        self.age = age
        self.gender = gender
        self.faculty = faculty
        self.live_in_dormitory = live_in_dormitory
        self.bio = bio
        self.interests = interests

    def add_dialog(self, dialog: Dialog):
        self.dialogs.append(dialog)
    def remove_dialog(self, dialog: Dialog):
        self.dialogs.remove(dialog)

