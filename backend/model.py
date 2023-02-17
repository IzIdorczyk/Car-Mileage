from pydantic import BaseModel

class Mileage(BaseModel):
    plate: str
    year: int
    month: int
    mileage: int

class Car(BaseModel):
    model: str
    plate: str
