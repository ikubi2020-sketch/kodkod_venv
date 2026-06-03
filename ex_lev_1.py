# Create main.py, import FastAPI, create app
# 2. Define the relevant functions for the routs
# 3. Return the dict for each URL
# 4. Run with uvicorn, test with curl | python script | swagger

from fastapi import FastAPI, HTTPException
from datetime import datetime
from operator import itemgetter
#--------------------------------1-----------------------------

# aff = FastAPI()

# @aff.get("/ping")
# def get_status():
#     return {"status" : "pong"}

# @aff.get("/greet/{name}")
# def greetings(name):
#     return  {"message": f"Hello, {name}!"}

#-----------------------------2-------------------------------

# poo = FastAPI()

# @poo.get("/icp")
# def icp_getter():
#     return {"service": "my-api", "version": "1.0"}

# @poo.get("/users/admin")
# def admin_type():
#     return {"role": "admin", "access": "full"}

# @poo.get("/users/{user_id}")
# def get_user(user_id):
#     return {"user id" : {user_id}, "name" : "momo", "email" : f"{user_id}.co2"}

#--------------------------------3-------------------------------------

# bear = FastAPI()

# @bear.get("/calc/{a}/{op}/{b}")
# def calc(a :int, op :str, b :int):
#     result = 0
    # if op == "+":
    #     result = a + b
    # elif op == "-":
    #     result = a + b
    # elif op == "*":
    #     result = a * b
    # elif op == "/":
    #     if b == 0:
    #         raise HTTPException(status_cod=400, detail = "cannot divide by 0")
    #     else:
    #         result = a / b
    # else:
    #     raise HTTPException(status_code=400, detail = "you are stupid")
    # return {"operator" : op, "result" :{result}}

#-------------------------4-----------------------------

# @bear.get("/status")
# def stat():
#     return {"system status" : f"the time is {datetime.now()}"}

#----------------------5--------------------------------
grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

miki = FastAPI()

@miki.get("/students/top")
def get_max_student():
    max_student = max(grades.values(), key=itemgetter("grade"))
    return {"the best student is" : f"{max_student}"}

@miki.get("/students")
def get_name():
    students = []
    for val in grades.values():
        students.append(val["name"])
    return {"students" : students}


@miki.get("/students/average")
def avg_students():
    avg = 0 
    for key in grades:
        avg += grades[key]["grade"]
    final_avg = avg / len(grades)
    return final_avg

@miki.get("/students/count")
def get_count():
    return {"the number student in class is" : {len(grades)}}

@miki.get("/students/{student_id}")
def get_by_id(student_id):
    for key in grades:
        if key == student_id:
            return grades[key]
    return  {"result" : "no student was found"}
