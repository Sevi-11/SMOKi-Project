from fastapi import FastAPI

app = FastAPI(title="SMOKi API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to SMOKi API Phase 1"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

