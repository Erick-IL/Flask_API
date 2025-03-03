from flask import Blueprint, request, jsonify
from app.models.user import register_user, get_all_users, search_user, update_user, delete_user


blueprint = Blueprint('users', __name__, url_prefix='/v1')

@blueprint.get('/get-users')
def users():
    result, success = get_all_users()
    return jsonify(result), success
    
@blueprint.post('/auth/signup')
def register():
    user_data = request.get_json(silent=True)
    result, success = register_user(user_data)
    return jsonify(result), success

@blueprint.get('/get-user/<user_info>')
def get_user_by_id(user_info):
    result, success = search_user(user_info)
    return jsonify(result), success

@blueprint.patch('/users/<user_info>')
def update(user_info):
    user_data = request.get_json(silent=True)
    result, success = update_user(user_info, user_data)
    return jsonify(result), success

@blueprint.delete('/users/<user_info>')
def delete(user_info):
    result, success = delete_user(user_info)
    return jsonify(result), success
