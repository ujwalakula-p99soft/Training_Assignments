from pydantic import BaseModel,EmailStr

class User(BaseModel):
    username:str
    email:EmailStr
    password:str

class User_Update(BaseModel):
    username:str
    password:str