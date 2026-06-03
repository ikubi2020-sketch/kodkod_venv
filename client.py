import requests 

respond = requests.get("http://127.0.0.1:8000/up_obj/15")

print(respond.status_code)
print(respond.json())

