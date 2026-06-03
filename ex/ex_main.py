from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_all():
    return {"any": "massage"}


@app.get("/items")
def get_all():
    return {"any": "massage"}