from flask import Blueprint, request, jsonify
from app.models.auth import login_user

blueprint = Blueprint("auth", __name__, url_prefix="/v1")

@blueprint.get('/auth/login')
def login():
    data = request.get_json(silent=True)
    result, status = login_user(data)
    return jsonify(result), status




    
    
    



