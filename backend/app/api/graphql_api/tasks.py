from fastapi import APIRouter

router=APIRouter(prefix="/tasks")


@router.get("/")
def create_access_token():
    pass


@router.get("/{comment_id}")
def create_access_token():
    pass

@router.post("/")
def create_refresh_token():
    pass


@router.put("/{comment_id}")
def create_refresh_token():
    pass


@router.delete("/{comment_id}")
def create_refresh_token():
    pass


@router.delete("/")
def create_refresh_token():
    pass