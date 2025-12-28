from pydantic import BaseModel
class SubTaskStatus(str,Enum):
    CREATED="created"
    INPROGRESS="in progress"
    COMPLETED="completed"

class TaskStatus(str,Enum):
    CREATED="created"
    INPROGRESS="in progress"
    COMPLETED="completed"
class SubTask(BaseModel):
    id: str
    task_id:str
    title:str
    description: str
    status: SubTaskStatus

class Task(BaseModel):
    id: str
    heading:str
    description:str
    sub_tasks:list(Task)
    status: TaskStatus
