from typing import Optional
from typing import Mapped
from typing import String
class User():
    fullname=Mapped[Optional[str]]
    def __repr__(self)->str:
        return f"User {self.fullname}"