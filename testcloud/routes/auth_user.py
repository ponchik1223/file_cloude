import fastapi 
from testcloud.registration_user.schema_user import UserCreate, UserRead
from testcloud.registration_user.auth import auth_backend
from fastapi_users import fastapi_users
from fastapi_users import FastAPIUsers
from testcloud.registration_user.model_user import User
from testcloud.registration_user.manager import get_user_manager


router_auth = fastapi.APIRouter()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router_auth.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


router_auth.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

