from flask import request, jsonify
from app.commons.jwt import decode_token
from flask_openapi3 import OpenAPI, Info
from app.controller import users
from app.controller import auth
from app.documentation.Api_v1 import auth_doc
from dotenv import load_dotenv
from http import HTTPStatus
import os


load_dotenv()
info = Info(title="API CRUD de usuários", version="v1")
app = OpenAPI(__name__, info=info, doc_ui="scalar", doc_prefix='/v1-docs')
app.register_blueprint(users.blueprint)
app.register_blueprint(auth.blueprint)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# API doc register 
app.register_api(auth_doc.blueprint)

@app.before_request
def verify_token():
    public_routes = ['/v1/auth/login', '/v1-docs', '/v1/users/']

    if any(request.path.startswith(route) for route in public_routes  or request.method == "OPTIONS"):
        return

    token = None

    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return jsonify({"message": "Token ausente"}), HTTPStatus.FORBIDDEN

    data = decode_token(token)
    if isinstance(data, tuple):
         return data
    
    request.user = data

@app.route('/')
def home():
    return "Flask está funcionando!"

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000, debug=True)









