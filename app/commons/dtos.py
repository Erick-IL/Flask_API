from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional
from http import HTTPStatus 

class UserSignup(BaseModel):
    name: str = Field(..., title="Username", min_length=2, example='Roger Silva')
    email: EmailStr = Field(..., title="User Email", example='roger.exemplo@gmail.com')
    password: str = Field(..., title="Password", min_length=8, example='password123')

class Userlogin(BaseModel):
    email: EmailStr = Field(..., title="User Email", example='roger.exemplo@gmail.com')
    password: str = Field(..., title="Password", min_length=8, example='password123')

class Token(BaseModel):
    Authorization: str = Field(..., title='Authorization', example='Bearer [Token]')

class get_user(BaseModel):
    Authorization: str = Field(..., title='Authorization', example='Bearer [Token]')



def validate_login(data):
    try:
        Userlogin(**data)
        return None, HTTPStatus.OK
    except ValidationError as e:
        return e.errors(), HTTPStatus.UNPROCESSABLE_ENTITY

def validate_new_user(data):
    try:
        UserSignup(**data)
        return None, HTTPStatus.OK
    except ValidationError as e:
        return e.errors(), HTTPStatus.UNPROCESSABLE_ENTITY

