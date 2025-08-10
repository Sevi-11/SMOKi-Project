from fastapi import FastAPI
from database import database
from pymongo.errors import ServerSelectionTimeoutError
app = FastAPI(title="SMOKi API", version="1.0")

@app.on_event("startup")
async def startup_db_check():
    try:
        await database.command("ping")
        print("✅ Successfully connected to MongoDB!")
    except ServerSelectionTimeoutError as e:
        print(f"❌ Could not connect to MongoDB: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to SMOKi API Phase 1"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/items")
async def get_items():
    items = await database.items.find().to_list(100)
    return items
