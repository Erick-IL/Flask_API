from flask import Flask, request, jsonify
from app.commons.jwt import decode_token
from app.controller import users
from app.controller import auth
from dotenv import load_dotenv
from http import HTTPStatus
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(users.blueprint)
app.register_blueprint(auth.blueprint)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.before_request
def verify_token():
    public_routes = ['/auth/login']

    if request.path in public_routes or request.method == "OPTIONS":
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









