from fastapi import FastAPI, HTTPException
from app.storage import MemoryStorage

app = FastAPI(title="Memory-In Service")

storage = MemoryStorage()

@app.post("/set")
def set_value(key: str, value: str):
    storage.set(key, value)
    return {"message": "Value stored successfully"}

@app.get("/get/{key}")
def get_value(key: str):
    value = storage.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}
