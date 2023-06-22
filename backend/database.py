from model import Car, Mileage

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.CarMileage

# Car collection
car_collection = database.car

async def fetch_one_car(plate):
    return await car_collection.find_one({"plate":plate})

async def fetch_all_cars():
    return [Car(**document) async for document in car_collection.find({})]

async def create_car(car):
    await car_collection.insert_one(car)
    return car

async def update_car(plate, new_plate):
    await car_collection.update_one({"plate":plate}, {"$set": {"plate":new_plate} })
    return await car_collection.find_one({"plate":new_plate})

async def remove_car(plate):
    await car_collection.delete_one({"plate":plate})
    return True



# Mileage collection
mileage_collection = database.mileage


async def fetch_all_mileages():
    return [Mileage(**document) async for document in mileage_collection.find({})]

async def fetch_one_mileage(plate, year, month):
    return await mileage_collection.find_one({"plate":plate, "year":year, "month":month})

async def fetch_all_car_mileages(plate):
    return [Mileage(**document) async for document in mileage_collection.find({"plate":plate})]

async def create_mileage(mileage):
    await mileage_collection.insert_one(mileage)
    return mileage

async def update_mileage(plate, year, month, mileage):
    await mileage_collection.update_one({"plate":plate, "year":year, "month":month}, {"$set": {"mileage":mileage} })
    return await mileage_collection.find_one({"plate":plate, "year":year, "month":month})

async def remove_mileage(plate, year, month):
    await mileage_collection.delete_one({"plate":plate, "year":year, "month":month})
    return True


#Date
async def find_all_mileages_in_month(year, month):
    cars = await fetch_all_cars()
    mils = []
    for car in cars:
        if await fetch_one_mileage(car.plate, year, month):
            mil = await fetch_one_mileage(car.plate, year, month)
            mils.append([car.plate, mil['mileage']])
            # mils.append({car.plate: mil['mileage']})
    return mils
