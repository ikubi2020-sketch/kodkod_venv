from fastapi import FastAPI

from utils.helper import * 
from utils.files_work import *
from logger_config import logger

app = FastAPI()

@app.post("/soldier")
def make_new(body: dict):
    create_soldier_utils(body)
    return {"result" : "soldier created"}



