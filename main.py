#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body , Query

app = FastAPI()

#Models

class Person(BaseModel):
    first_name : str
    last_namet :str
    age :int
    is_married : Optional[bool] =None
    hair_color : Optional[str]= None
    


@app.get("/")
def home():
    return {"Hello": "World"}


#request and response  Body


@app.post("/person/new")
def create_person(person : Person = Body(...)):
    
    return person
    


#Validations Query parameters

@app.get("/person/detail")
def show_person(
    
    name: Optional[str] = Query (default= None, min_length= 1, max_length=50),
    age: int = Query(...)
    
):
    return {name : age}