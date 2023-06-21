from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Car, Mileage
from database import (
    fetch_one_car,
    fetch_all_cars,
    create_car,
    update_car,
    remove_car,
    fetch_one_mileage,
    fetch_all_mileages,
    fetch_all_car_mileages,
    create_mileage,
    update_mileage,
    remove_mileage)

# App object
app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.get('/')
def read_root():
    return {"Hello" : "World"}


@app.get("/cars", tags=['Car'])
async def get_cars():
    return await fetch_all_cars()


@app.get("/car/{plate}", response_model=Car, tags=['Car'])
async def get_car_by_plate(plate):
    response = await fetch_one_car(plate)
    if response:
        return response
    raise HTTPException(404, f"Car with {plate} plate number doesn't exist in our database")


@app.post("/car/", response_model=Car, tags=['Car'])
async def post_car(car: Car):
    if await fetch_one_car(car.plate):
        raise HTTPException(409, f"Car with {car.plate} plate number already exist in our database")
    if len(car.plate.split()) < 4:
        raise HTTPException(411, f"your plate number '{car.plate}' is too short")
    response = await create_car(car.dict())
    if not response:
        raise HTTPException(400, "Something went wrong or Bad Request")
    return response


@app.put("/car/{plate}", response_model=Car, tags=['Car'])
async def put_car(plate:str, new_plate:str):
    response = await update_car(plate, new_plate)
    if response:
        return response
    raise HTTPException(404, f"Car with {plate} plate number doesn't exist in our database")


@app.delete("/car/{plate}", tags=['Car'])
async def delete_car(plate):
    response = await remove_car(plate)
    if response:
        return f"Succesfully deleted car with {plate} plate numbers!"
    raise HTTPException(404, f"Car with {plate} plate number doesn't exist in our database")

###
### Mileages
###

@app.get("/cars/mileages", tags=['Mileages'])
async def get_all_mileages():
    return await fetch_all_mileages()


@app.get("/car/{plate}/{year}/{month}/mileage", response_model=Mileage, tags=['Mileages'])
async def get_one_mileage(plate:str, year:int, month:int):
    response = await fetch_one_mileage(plate, year, month)
    if response:
        return response
    raise HTTPException(404, f"Mileage in {month}.{year} from car with {plate} plate number doesn't exist in our database")


@app.get("/car/{plate}/mileages", tags=['Mileages'])
async def get_mileages_by_plate(plate):
    response = await fetch_all_car_mileages(plate)
    if response:
        return response
    raise HTTPException(404, f"We don't have any mileage for car with {plate} plate number")


@app.post("/car/{plate}/mileage", response_model=Mileage, tags=['Mileages'])
async def post_mileage(mileage: Mileage):
    if await fetch_one_mileage(mileage.plate, mileage.year, mileage.month):
        raise HTTPException(409, f"Recodr for car with {mileage.plate} plate number in {mileage.month}.{mileage.year} already exist in our database")
    response = await create_mileage(mileage.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong or Bad Request")


@app.put("/car/{plate}/{year}/{month}", response_model=Mileage, tags=['Mileages'])
async def put_mileage(plate:str, year:int, month:int, mileage:int):
    response = await update_mileage(plate, year, month, mileage)
    if response:
        return response
    raise HTTPException(404, f"Mileage in {month}.{year} from car with {plate} plate number doesn't exist in our database")


@app.delete("/car/{plate}/{year}/{month}", tags=['Mileages'])
async def delete_mileage(plate:str, year:int, month:int):
    response = await remove_mileage(plate, year, month)
    if response:
        return f"Succesfully deleted mileage in {month}.{year} from car with {plate} plate numbers!"
    raise HTTPException(404, f"Mileage in {month}.{year} from car with {plate} number plate doesn't exist in our database")