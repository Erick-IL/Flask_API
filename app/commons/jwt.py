from dotenv import load_dotenv
import datetime
import jwt
import os

      
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def generate_token(user):
    payload = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"message": "token expirado"}, 401
    except jwt.InvalidTokenError:
        return {"message": "token invalido"}, 401
