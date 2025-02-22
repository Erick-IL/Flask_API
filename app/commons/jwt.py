from dotenv import load_dotenv
from http import HTTPStatus
import datetime
import jwt
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


def generate_token(user):
    payload = {
        'id': user['id'],
        'name': user['name'],
        'email': user['email'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        'iss': 'Flask_API',
        'aud': 'Users'
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token

def decode_token(token):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], issuer="Flask_API", audience="Users")
        return decode_token
    except jwt.ExpiredSignatureError:
        return {"message": "token expirado"}, HTTPStatus.UNAUTHORIZED
    except jwt.InvalidTokenError:
        return {"message": "token invalido"}, HTTPStatus.UNAUTHORIZED

