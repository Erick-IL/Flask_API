from dotenv import load_dotenv
import datetime
import jwt
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


def encode_jwt(payload):
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(encoded_jwt):
    jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])