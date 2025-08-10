from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/smoki_db")

client = AsyncIOMotorClient(MONGO_URI)
database = client.get_database("smoki_db")
