from pydantic import BaseModel
from datetime import datetime


class Mileage(BaseModel):
    plate: str
    year: int
    month: int
    mileage: int

    class Config:
        schema_extra = {
            'example': {
                'plate': 'GD 229TY',
                'year': datetime.now().year,
                'month': datetime.now().month,
                'mileage': 68358
            }
        }


class Car(BaseModel):
    model: str
    plate: str

    class Config:
        schema_extra = {
            'example': {
                'model': 'Fabia',
                'plate': 'GD 229TY'
            }
        }


# class LastRecordPerModel(BaseModel):
#     model: str
#     plate: str
#     mileage: int
#     month: int
#     year: int
#
#     class Config:
#         schema_extra = {
#             'example': {
#                 "model": "Skoda Scala",
#                 "plate": "GD448XT",
#                 "mileage": 36001,
#                 "month": 11,
#                 "year": 2023
#             }
#         }