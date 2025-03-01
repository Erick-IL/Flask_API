from flask import Flask, jsonify, request
from flask_openapi3 import APIBlueprint, Tag
from app.commons.dtos import UserSignup
from pydantic import BaseModel, EmailStr, Field, ValidationError

blueprint = APIBlueprint("api", __name__, url_prefix="/v1")

tag_auth = Tag(name="Auth Jwt", description="Rotas para funcionamento do Jwt authenticator")

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@blueprint.post(
    "/users/",
    summary="Create a User",
    description="Time to create a user account, eh?",
    tags=[tag_auth],
    security=[{"BearerAuth": []}],
    responses={
        201: {"description": "Usuário criado com sucesso."},
        400: {"description": "Bad Request - Campos ausentes."},
        422: {"description": "Unprocessable Entity - Campos inválidos."}
    }
)
def signup(body: UserSignup):
    return