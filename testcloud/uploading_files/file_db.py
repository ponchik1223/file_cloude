from testcloud.uploading_files.model_file import user_file
from datetime import datetime
from sqlalchemy import insert, select
import os
from testcloud.config import PERSISTENT_STORAGE
import csv
import hashlib

async def upload_file_db(received_file: dict):
    
    user = received_file["user"].id
    if not os.path.exists(PERSISTENT_STORAGE + "/" +  str(user)):
            os.makedirs(PERSISTENT_STORAGE + "/" + str(user))
    
    
    file_content = received_file["upload_file"].file.read()
    
    crypt = hashlib.sha1()
    crypt.update(file_content)
    location = crypt.hexdigest()
         
    with open(f"{PERSISTENT_STORAGE}/{user}/{location}", "wb+") as file_object:
        file_object.write(file_content)

    stmt = insert(user_file).values(name_file=received_file["upload_file"].filename,
                                    upload_date=datetime.utcnow(),
                                    user_id=user,
                                    location_file=location)
    
    await received_file["session"].execute(stmt)
    await received_file["session"].commit()
    
    return 1


# получение списка файлов с наименование столбоцов
async def getting_user_files(info_user: dict):
    
    query = select(user_file).where(user_file.c.user_id == info_user["user_id"])
    result = await info_user["session"].execute(query)

    # собираем инофрмацию о файлах пользователя
    records = [tuple(d) for d in result]

    answer_list = []
    
    for (filename,file_location,ts, user_id) in records:
        with open(f"{PERSISTENT_STORAGE}/{user_id}/{file_location}") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            dict_from_csv = dict(list(csv_reader)[0])
            list_of_column_names = list(dict_from_csv.keys())

            iter_file = {
                    'name_file': filename,
                    'upload_date': str(ts),
                    'column_name': list_of_column_names
                 }
            

            answer_list.append(iter_file)

    
    return answer_list

