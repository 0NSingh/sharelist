from .auth import router as auth_router
from .comments import router as comments_router
from .tasks import router as tasks_router
from .user import router as user_router

__all__=[
    "auth_router",
    "comments_router",
    "tasks_router",
    "user_router"
]