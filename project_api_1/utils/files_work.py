from logger_config import logger
import  json

def return_soldiers()-> list:
    with open("soldiers.json",  "r", encoding="utf-8")as file:
        soldiers_dict = file.load
        return soldiers_dict

def create_soldier(body)-> None:
    with open("soldiers.json",  "r", encoding="utf-8")as file:
        soldiers_dict = json.load(file)
        soldiers_id = str(body["id"])
        soldiers_dict[soldiers_id] = body
    with open("soldiers.json", "w", encoding="utf-8")as file:
        json.dump(soldiers_dict, file, indent=2)
        logger.info("soldier created")
    return None

def get_soldier(id)-> dict:
    with open("soldiers.json", "r", encoding="utf-8")as file:
        for soldier in file:
            if soldier["id"] == id:
                return soldier , True

def get_soldiers()-> list:
    with open("soldiers.json",  "a", encoding="utf-8")as file:
        logger.info("all soldiers details send out")
        return file

def update_soldier(id, upd_key, upd_val)-> None:
    with open("soldiers.json",  "a", encoding="utf-8")as file:
        for line in file:
            if line["id"] == id:
                line[upd_key] = upd_val
                logger.info("soldier details updated")
    return False



