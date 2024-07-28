from dataclasses import dataclass
from typing import List
import Profile
import Dialog


@dataclass
class User:
    user_id: int
    username: str
    email: str
    password: str
    profile: Profile = None  # Связь с профилем пользователя
    dialogs: List[Dialog] = None  # Связь с диалогами пользователя
    liked_list: List[int] = None  # Список пользователей, которых он лайкнул
    black_list: List[int] = None  # Списко пользователей, которых он забанил
    matched_list: List[int] = None  # Список взаимных семпатий

    def __post_init__(self):
        if self.dialogs is None:
            self.dialogs = []
        if self.liked_list is None:
            self.liked_list = []
        if self.black_list is None:
            self.black_list = []
        if self.matched_list is None:
            self.matched_list = []