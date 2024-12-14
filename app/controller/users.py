from flask import Blueprint, request, jsonify
from app.models.user import register_user, get_all_users, search_user


blueprint = Blueprint('users', __name__)

@blueprint.route('/users', methods={"GET", "POST"})
def users():
    if request.method == 'GET':
        data = get_all_users()
        print(jsonify(data))
        return jsonify(data)
    if request.method == 'POST':
        data = register_user()
        return jsonify(data)


@blueprint.route('/users/<int:id>', methods={'GET'})
def get_user_by_id(id):
    data = search_user(id)
    return data

