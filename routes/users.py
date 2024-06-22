from fastapi.routing import APIRouter, Request
from utils.limiter import limiter

user_router = APIRouter()

@user_router.get('/user')
@limiter.limit('5/minute')
def test_user(request : Request):
    return {'msg': 'this is test for user route'}