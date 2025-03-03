from app.commons.dtos import validate_login
from app.commons.jwt import generate_token
from app.models.user import search_user
from flask import request
from http import HTTPStatus



def login_user(auth_data):
    error, status = validate_login(auth_data)
    if status == HTTPStatus.UNPROCESSABLE_ENTITY:
        return {'message': error}, HTTPStatus.UNPROCESSABLE_ENTITY
    
    auth_data = request.get_json()
    if not auth_data or not auth_data['email'] or not auth_data['password']:
        return {'message': 'email e senha necessario'}, HTTPStatus.BAD_REQUEST
    
    user_info, status = search_user(auth_data['email'])
    if status != HTTPStatus.OK or user_info["password"] != auth_data["password"]:
        return {'message': 'Credenciais invalidas'}, HTTPStatus.UNAUTHORIZED
    
    token = generate_token(user_info)
    return {"token": token}, HTTPStatus.OK