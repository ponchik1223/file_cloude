from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey
from testcloud.database import metadata

from testcloud.registration_user.model_user import user as user_model


user_file = Table(
    "user_file",
    metadata,
    Column("name_file", String, nullable=False),
    Column("location_file", String, nullable=True),
    Column("upload_date", TIMESTAMP, default=datetime.utcnow),
    Column("user_id", Integer, ForeignKey(user_model.c.id)),
)
