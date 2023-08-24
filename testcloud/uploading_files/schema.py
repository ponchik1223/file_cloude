from pydantic import BaseModel

from datetime import datetime


class OperationSchema(BaseModel): 
    
    name_file: str
    upload_date: datetime
    location_file: str

    class Config:
        from_attributes = True