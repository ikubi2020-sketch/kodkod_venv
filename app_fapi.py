from fastapi import FastAPI 
import uvicorn
app = FastAPI()

@app.get("/")
def read_line():
    return {"key line" : "value line"}

@app.get("/up_obj/{item}")
def up_obj(item):
    return {"in id " : item, "the id is " : item}


if __name__ == "__main__":
    uvicorn.run("app_fapi:app", host="127.0.0.1", port=8000,reload=True)

# What does HTTP status code 404 mean?

# The resource was not found

# In FastAPI, what does @app.get("/items/{item_id}") define?

# b) A GET route that captures a value from the URL

# Which command starts a FastAPI server with auto-reload?

# c) uvicorn main:app --reload

