from fastapi import FastAPI
from app.api import user_router,auth_router,tasks_router,comments_router

app=FastAPI()


app.include_router(prefix="/api/v1",router=user_router, tags=["user"])
app.include_router(prefix="/api/v1",router=tasks_router, tags=["tasks"])
app.include_router(prefix="/api/v1",router=comments_router, tags=["comments"])
app.include_router(prefix="/api/v1",router=auth_router, tags=["auth"])
