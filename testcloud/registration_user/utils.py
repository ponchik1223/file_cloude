from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from testcloud.database import get_async_session
from fastapi import Depends

from testcloud.registration_user.model_user import User
# from uploading_files.model_file import user_file

#аккумуляция данных

# metadata = [user.metadata, user_file.metadata]


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)