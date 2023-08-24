from fastapi import FastAPI
from .routes.auth_user import router_auth # последнее нам нужно для протект метода
from .routes.load_file import router_fiel

app = FastAPI(
    title="file_sharing"
)
app.include_router(router_auth)
app.include_router(router_fiel)

