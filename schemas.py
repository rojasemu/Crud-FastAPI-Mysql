#Pydantic

from pydantic import BaseModel, EmailStr
from pydantic import Field

#Python
from typing import Optional
from enum import Enum



#Models
class UserRequestModel(BaseModel):
    username : str = Field(
        ...,
        min_length=1,
        max_length=60        
    )
    email : EmailStr
    
    
class UserResponseModel(UserRequestModel): # con esta clase nos permite serializar   
    id : int     


class UserUpdate(BaseModel):
    username : str = Field(
        ...,
        min_length=1,
        max_length=60        
    )
    email : EmailStr















class HairColor(Enum):
    white ="white"
    brown ="bronw"
    black = "black"
    blonde = "blonde"
    red = "red"
    

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=60,
        example ="El Tigre"
        )
    state : str = Field(
           ...,
        min_length=1,
        max_length=60,
        example ="Anzoategui"
        )
    country : str = Field(
           ...,
        min_length=1,
        max_length=60,
        example ="Venezuela"
        )

class Person(BaseModel):
    first_name : str = Field (
        ...,
        min_length=1,
        max_length=50,
        example ="Erik" 
        )
    last_namet :str =Field(
        ...,
        min_length=1,
        max_length=50,
        example = "Rojas"
        )
    age :int = Field(
        ...,
        gt=0,
        le=115,
        example = 36
        
        )
    is_married : Optional[bool] = Field(default=None, example = False)
    hair_color : Optional[HairColor]= Field (default=None, example = "black")
    
    
    
    # class Config: # esta subclase nos permite tener un valores por default en el body
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "García Martoni",
    #             "age": 21, 
    #             "hair_color": "blonde",
    #             "is_married": False
    #         }
    #     }
