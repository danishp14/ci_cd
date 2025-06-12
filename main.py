from fastapi import FastAPI

app = FastAPI()

@app.get("/api/get_message")
def read_root():
    return {"message": "Hello, FastAPI"}