from fastapi import APIRouter

router=APIRouter()


@router.post("/token")
def create_access_token():
    pass


@router.post("/refresh")
def create_refresh_token():
    pass