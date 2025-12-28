class Comments(BaseModel):
    id:Optional[str]
    task_id:str
    text:str
    is_edited:bool
    user_id:str