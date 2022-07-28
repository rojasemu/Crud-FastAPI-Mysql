#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body , Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
    white ="white"
    brown ="bronw"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str
    state : str
    country : str

class Person(BaseModel):
    first_name : str = Field (
        ...,
        min_length=1,
        max_length=50 
        )
    last_namet :str =Field(
        ...,
        min_length=1,
        max_length=50
        )
    age :int = Field(
        ...,
        gt=0,
        le=115
        )
    is_married : Optional[bool] = Field(default=None)
    hair_color : Optional[HairColor]= Field (default=None)
    


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



#validations request body

@app.put("/person/{person_id}")
def update_person(
    
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID It's required"
    ),
    
    person: Person = Body(...),
    location :Location = Body(...)    
):
    results = person.dict()
    results.update(location.dict())    
    return results