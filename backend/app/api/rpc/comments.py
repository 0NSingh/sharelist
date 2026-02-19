from fastapi import APIRouter

router=APIRouter()

@router.get("/comments")
def create_access_token():
    pass


@router.get("/comments/{comment_id}")
def create_access_token():
    pass

@router.post("/comments")
def create_refresh_token():
    pass


@router.put("/comments/{comment_id}")
def create_refresh_token():
    pass


@router.delete("/comments/{comment_id}")
def create_refresh_token():
    pass


@router.delete("/comments")
def create_refresh_token():
    pass