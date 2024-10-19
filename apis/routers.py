from fastapi import APIRouter

from apis.user.views import user_list

router = APIRouter(prefix='/api')
user = APIRouter(prefix='/user', tags=['用户管理'])

user.get('/list', summary='用户列表')(user_list)

router.include_router(user)
