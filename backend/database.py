from model import Car, Mileage

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.CarMileage

# Car collection
car_collection = database.car

async def fetch_one_car(plate):
    document = await car_collection.find_one({"plate":plate})
    return document

async def fetch_all_cars():
    cars = []
    cursor = car_collection.find({})
    async for document in cursor:
        cars.append(Car(**document))
    return cars


async def create_car(car):
    document = car
    result = await car_collection.insert_one(document)
    return document

async def update_car(plate, new_plate):
    await car_collection.update_one({"plate":plate}, {"$set": {"plate":new_plate} })
    document = await car_collection.find_one({"plate":new_plate})
    return document

async def remove_car(plate):
    await car_collection.delete_one({"plate":plate})
    return True



# Mileage collection
mileage_collection = database.mileage


async def fetch_all_mileages():
    mileages = []
    cursor = mileage_collection.find({},)
    async for document in cursor:
        mileages.append(Mileage(**document))
    return mileages

async def fetch_one_mileage(plate, year, month):
    document = await mileage_collection.find_one({"plate":plate, "year":year, "month":month})
    return document

async def fetch_all_car_mileages(plate):
    mileages = []
    cursor = mileage_collection.find({"plate":plate})
    async for document in cursor:
        mileages.append(Mileage(**document))
    return mileages

async def create_mileage(mileage):
    document = mileage
    result = await mileage_collection.insert_one(document)
    return document

async def update_mileage(plate, year, month, mileage):
    await mileage_collection.update_one({"plate":plate, "year":year, "month":month}, {"$set": {"mileage":mileage} })
    document = await mileage_collection.find_one({"plate":plate, "year":year, "month":month})
    return document

async def remove_mileage(plate, year, month):
    await mileage_collection.delete_one({"plate":plate, "year":year, "month":month})
    return True