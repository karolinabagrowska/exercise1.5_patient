from fastapi import FastAPI
from fastapi import FastAPI, Response, status
from fastapi import FastAPI, HTTPException
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse

class Person(BaseModel):
    name: str
    surname: str

class Counter():
    id = 0


app = FastAPI()
app.patients = {}

@app.post("/register")
def register_post(response: Response, person: Person):
    
    register_date = date.today()
    print(register_date)
    #print(type(register_date))
    new_name = []
    new_surname = []
    for x in person.name:
        if x.isalpha():
            new_name.append(x)
        else:
            continue
    
    for y in person.surname:
        if y.isalpha():
            new_surname.append(y)
        else:
            continue
    name_len = len(new_name)
    surname_len = len(new_surname)
    
    vaccination_date = register_date + timedelta(name_len) + timedelta(surname_len)

    Counter.id += 1


    dict_new = {
        "id": Counter.id,
        "name": person.name,
        "surname": person.surname,
        "register_date": str(register_date),
        "vaccination_date": str(vaccination_date)
    }

    app.patients[Counter.id] = dict_new
    
    response.status_code = status.HTTP_201_CREATED

    return dict_new

@app.get("/patient/{id}")
def get_id(response: Response, id: int):
    if id in app.patients.keys():
        return JSONResponse(content=app.patients[id], status_code=200)
    elif id < 1:
        raise HTTPException(status_code=400)
    else:
        raise HTTPException(status_code=404)

        