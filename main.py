from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the VPS Test Server!"}

@app.get("/cpu")
def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    return {
        "cpu_usage_percent": cpu_usage,
        "cpu_count": cpu_count
    }

@app.get("/memory")
def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "total_memory": memory.total,
        "available_memory": memory.available,
        "used_memory": memory.used,
        "memory_usage_percent": memory.percent
    }

@app.get("/disk")
def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "total_disk_space": disk.total,
        "used_disk_space": disk.used,
        "free_disk_space": disk.free,
        "disk_usage_percent": disk.percent
    }
