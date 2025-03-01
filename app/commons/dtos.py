from pydantic import BaseModel, EmailStr, Field, ValidationError
from http import HTTPStatus 
from flask import Flask, jsonify, request

class UserSignup(BaseModel):
    name: str = Field(..., title="Nome do usuário", min_length=2, example='Roger Silva')
    email: EmailStr = Field(..., title="Email do usuário", example='roger.exemplo@gmail.com')
    password: str = Field(..., title="Senha", min_length=8, example='password123')

def validation(data):
    try:
        UserSignup(**data)
        return None, HTTPStatus.OK
    except ValidationError as e:
        return e.errors(), HTTPStatus.UNPROCESSABLE_ENTITY
    
data_teste = {
    "name": "roger3",
    "email": "ro@gmail.com",
    "password": "senha123"
}

validation(data_teste)
