from fastapi import Depends, UploadFile, File, APIRouter
from testcloud.registration_user.model_user import User
from testcloud.routes.auth_user import fastapi_users
from sqlalchemy.ext.asyncio import AsyncSession
from testcloud.database import get_async_session
from testcloud.uploading_files import file_db

from fastapi.responses import JSONResponse

current_user = fastapi_users.current_user()
router_fiel = APIRouter()

#загрузка файлов для авторизованных пользователей
@router_fiel.post("/upload_file")
async def file_upload(user: User = Depends(current_user),
                      upload_file: UploadFile = File(...),
                      session: AsyncSession = Depends(get_async_session)
                       ):
    file_to_save = {"user": user,"upload_file" : upload_file,"session" : session}
    await file_db.upload_file_db(file_to_save)

    return f"{user.username} ваш файл сохранен"


# Получение списка файлов с информацией о колонках (для регистрированных пользователей)
@router_fiel.get("/uploading_user_files")
async def getting_files(user: User = Depends(current_user),
                        session: AsyncSession = Depends(get_async_session)
                       ):
    
    info_user = {"user_id": user.id, "session": session}
    result = await file_db.getting_user_files(info_user)
    return JSONResponse(result)