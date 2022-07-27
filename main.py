#Python
from importlib.resources import path
from operator import gt
from turtle import title
from typing import Optional
from unittest.mock import patch

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body , Query, Path

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
    


#Validations: Query parameters

@app.get("/person/detail")
def show_person(
    
    name: Optional[str] = Query (
        default= None, 
        min_length= 1, 
        max_length=50,
        title="Person Name",
        description="This is Person Name It's between 1 and 50 characters"
        ),
    age: int = Query (
         ...,
         title="Person Age",
         description="This is the Person Age  It's required"
         )    
):
    return {name : age}



#validations : path parameters

@app.get ("/person/detail/{person_id}")
def show_person(
    
    person_id:int = Path(
        ..., 
        gt=0,
        title="Person Id",
        description ="This is the Person Id It's required"        
        )
    
):
    return {person_id: "It exists"}