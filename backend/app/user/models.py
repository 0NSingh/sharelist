from fastapi import BaseModel
class Image(BaseModel):
    url: str
    name: str
class AccountStatus(str,Enum):
    ACTIVE="active"
    INACTIVE="inactive"

class UserRole(str, Enum):
    ADMIN = "admin"
    CREATOR="creator"
    EDITOR = "editor"
    VIEWER = "viewer"

class User(BaseModel):
    id:str
    email:str
    password:str
    bio:str
    username:str
    p_pic: Image | None = None
    acc_status: AccountStatus