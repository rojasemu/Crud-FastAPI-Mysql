
from enum import unique
from peewee import *


connection= MySQLDatabase(    
    'bdapi',
    user ='root',
    password = 'jeremy',
    host = 'localhost',
    port=3306     
)


class User(Model):
    
    username = CharField(max_length=50, unique =True)
    email = CharField(max_length=50)    
    
    def __str__ (self):
        return self.username
    
    class Meta:
        
        database =connection
        table_name = 'users'
        
        
