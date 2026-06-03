from logger_config import logger
from utils.files_work import *
from fastapi import HTTPException

def is_valid_create(body):
    logger.info("start checking body validation")
    if len(body) != 3 or type(body) != dict:
        logger.error("wrong format of details")
        raise HTTPException(status_code=400, detail="wrong format of details")
    elif "id" not in body.keys() or "personal_number" not in body.keys() or "role" not in body.keys():
        logger.error("missing key")
        raise HTTPException(status_code=400, detail="missing key")
    




def create_soldier_utils(body):
    create_soldier(body)

def get_soldier_utils(id):
    soldier , confirmation = return_soldiers()
    if confirmation == True:
        logger.info("soldier id {id} was found and sent out")
        return {"soldier" :{soldier}}
    else:
        logger.info("soldier id {id} was not found")
        raise HTTPException(status_code=400, detail="no soldier id {id} was found")      

def get_all_soldiers():
    file = return_soldiers()
    return {"all soldiers are" :{file}}

def update_soldier(id,):
    update = update_soldier(id)