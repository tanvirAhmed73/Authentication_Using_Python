from pydantic import BaseModel

class Auth_Msg_Response(BaseModel):
    message:str

class Auth_Data_Response(BaseModel):
    username:str
    email:str
    is_active:bool

class UserCreate(BaseModel):
    username:str
    password:str
    email:str
    is_active:bool

class UserLogin(BaseModel):
    email:str
    password:str


    