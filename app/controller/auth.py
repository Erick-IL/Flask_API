from flask import Blueprint, request, jsonify
from app.models.user import search_user
from app.commons.jwt import generate_token
from http import HTTPStatus

blueprint = Blueprint('auth', __name__)


@blueprint.get('/auth/login')
def login():
    auth_data = request.get_json()
    if not auth_data or not auth_data['email'] or not auth_data['password']:
        return {'message': 'email e senha necessario'}, HTTPStatus.BAD_REQUEST
    
    user_info, status = search_user(auth_data['email'])
    if status != HTTPStatus.OK or user_info["password"] != auth_data["password"]:
        return {'message': 'Credenciais invalidas'}, HTTPStatus.UNAUTHORIZED
    
    token = generate_token(user_info)
    return {"token": token}, HTTPStatus.OK






    
    
    



