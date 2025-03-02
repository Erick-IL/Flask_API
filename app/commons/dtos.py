from pydantic import BaseModel, EmailStr, Field, ValidationError
from http import HTTPStatus 

class UserSignup(BaseModel):
    name: str = Field(..., title="Nome do usuário", min_length=2, example='Roger Silva')
    email: EmailStr = Field(..., title="Email do usuário", example='roger.exemplo@gmail.com')
    password: str = Field(..., title="Senha", min_length=8, example='password123')

class Userlogin(BaseModel):
    email: EmailStr = Field(..., title="Email do usuário", example='roger.exemplo@gmail.com')
    password: str = Field(..., title="Senha", min_length=8, example='password123')


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

