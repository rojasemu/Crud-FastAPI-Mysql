

#Database
import email
from database import connection
from database import User


#Validations

from schemas import *


#FastAPI
from fastapi import FastAPI
from fastapi import Body , Query, Path, HTTPException

from schemas import UserRequestModel

app = FastAPI()

# Event Conection BD and close BD
@app.on_event('startup')
def startup ():
    if connection.is_closed():
        connection.connect()
        
    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()




@app.get("/")
def home():
    return {"Hello": "World"}


#request and response  Body

#Create user

@app.post("/users")
async def create_user(user_request: UserRequestModel):
    user = User.create(
        username = user_request.username,
        email = user_request.email    
    )
    
    return user_request
    


# Consult User
@app.get("/users/{user_id}")
async def get_user (user_id):
    
    user =User.select().where(User.id == user_id).first()    
    
    if user:        
        return UserResponseModel (id=user.id, username=user.username, email=user.email)# Serializando
    else:
        return HTTPException (404, "User Not Found")


#Delete User

@app.delete("/users/{user_id}")
async def delete_user (user_id):
    
    user =User.select().where(User.id == user_id).first()    
    
    if user:    
        user.delete_instance()    
        return "True"
    else:
        return HTTPException (404, "User Not Found")



#Update User

@app.put("/users/{user_id}")
async def update_user (user_id, user_update: UserUpdate ):
    
    #user =User.select().where(User.id == user_id).first()    
    
    connection.execute(User.update(
        
        username = user_update.username,
        email = user_update.email,  
    ).where(User.id == user_id))         
                       
    return connection.execute(User.select()).fetchall()

       
    
  
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